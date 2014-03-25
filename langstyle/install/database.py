#!/usr/bin/env python

import os
import re
from subprocess import Popen, PIPE
from mysql import connector as dbconnector
from .. import config

db_connection = config.database_connection.copy()
del db_connection["database"]

def _create_connection():
    return dbconnector.connect(**db_connection)

def _log_error(error_msg):
    config.service_factory.get_log_service().error(error_msg)

def _log_debug(msg):
    config.service_factory.get_log_service().debug(msg)

def _fetch_one(cursor):
    for result in cursor:
        if result:
            return result
    return None

def _execute_query_one(cmd_text):
    conn = None
    cursor = None
    try:
        conn = dbconnector.connect(**config.database_connection)
        cursor = conn.cursor()
        cursor.execute(cmd_text)
        return _fetch_one(cursor)
    except dbconnector.DatabaseError as db_error:
        _log_error(db_error.msg)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def _execute_non_query(cmd_text):
    conn = None
    cursor = None
    try:
        conn = _create_connection()
        cursor = conn.cursor()
        for statement in cmd_text.split(";"):
            if statement.strip():
                cursor.execute(statement)
        conn.commit()
        return True
    except dbconnector.DatabaseError as db_error:
        _log_error(db_error.msg)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return False

file_name_regex = re.compile(r"(?i)^([0-9]+)\.([0-9]+)\.([0-9]+)\-(.*)\.sql$")

def _file_number_compare(first_file_pattern, second_file_pattern):
    if first_file_pattern[0] > second_file_pattern[0]:
        return 1
    elif first_file_pattern[0] < second_file_pattern[0]:
        return -1
    if first_file_pattern[1] > second_file_pattern[1]:
        return 1
    elif first_file_pattern[1] < second_file_pattern[1]:
        return -1
    if first_file_pattern[2] > second_file_pattern[2]:
        return 1
    elif first_file_pattern[2] < second_file_pattern[2]:
        return -1
    return 0

def _get_file_number_pattern(file_pattern):
    return (int(file_pattern[0]), int(file_pattern[1]), int(file_pattern[2]))

def _file_compare(first_file_name, second_file_name):
    first_file_pattern = file_name_regex.findall(first_file_name)[0]
    second_file_pattern = file_name_regex.findall(second_file_name)[0]
    first_number_pattern = _get_file_number_pattern(first_file_pattern)
    second_number_pattern = _get_file_number_pattern(second_file_pattern)
    return _file_number_compare(first_number_pattern, second_number_pattern)

def _find_insert_index(sorted, file_name):
    for index in range(0, len(sorted)):
        if _file_compare(sorted[index], file_name) > 0:
            return index
    return len(sorted)

def _sort_files(files):
    sorted=[]
    for file_name in files:
        insert_index = _find_insert_index(sorted, file_name)
        sorted.insert(insert_index, file_name)
    return sorted

def _filter_file(file_name):
    if file_name_regex.match(file_name):
        return True
    return False

def _get_schema_file_names(dir):
    files = os.listdir(dir)
    return [file_name for file_name in files if _filter_file(file_name)]

def _get_sorted_schema_files(dir):
    try:
        schema_file_names = _get_schema_file_names(dir)
        sorted_schema_files = _sort_files(schema_file_names)
        return [os.path.join(dir, file_name) for file_name in sorted_schema_files]
    except FileNotFoundError as e:
        _log_error("directory "+ dir + " not found")

def _read_file(full_file_path):
    with open(full_file_path, "r") as f:
        return " ".join(f.readlines())

def _run_schema_files(file_paths):
    for file_path in file_paths:
        _run_schema_file(file_path)

def _run_schema_file(file_path):
    schema_content = _read_file(file_path)
    _log_debug(file_path)
    _execute_non_query(schema_content)

def _create_schema():
    schema_files = _get_sorted_schema_files(config.DATABASE_SCHEMA_DIR)
    _run_schema_files(schema_files)

def _get_procedure_files():
    dir = config.DATABASE_PROCEDURE_DIR
    files = os.listdir(dir)
    return [os.path.join(dir, file_name) for file_name in files]

def _create_procedure():
    procedure_files = _get_procedure_files()
    db_conn = config.database_connection.copy()
    for file in procedure_files:
        _log_debug(file)
        mysql_process = Popen("mysql -h%s -u%s -p%s -D%s < %s" % (db_conn["host"], db_conn["user"], db_conn["password"], db_conn["database"], file), stdout=PIPE, stdin=PIPE, shell=True)
        std_out, std_error = mysql_process.communicate()
        if std_error:
            _log_error(std_error)

def _get_upgrade_files(max_number_pattern):
    try:
        schema_dir = config.DATABASE_SCHEMA_DIR
        schema_file_names = _get_schema_file_names(schema_dir)
        sorted_schema_files = _sort_files(schema_file_names)
        for i in range(0, len(sorted_schema_files)):
            file_pattern = file_name_regex.findall(sorted_schema_files[i])[0]
            file_number_pattern = _get_file_number_pattern(file_pattern)
            if _file_number_compare(file_number_pattern, max_number_pattern) > 0:
                return sorted_schema_files[i:]
    except FileNotFoundError as e:
        _log_error("directory "+ schema_dir + " not found")
    return []

def _create_upgrade_schemas():
    select_schema_changes = "select MajorReleaseNumber, MinorReleaseNumber, BuildNumber from SchemaChange order by MajorReleaseNumber desc, MinorReleaseNumber desc, BuildNumber desc limit 0, 1;"
    max_db_schema = _execute_query_one(select_schema_changes)
    if max_db_schema:
        upgrade_files = _get_upgrade_files(max_db_schema)
    else:
        upgrade_files = _get_sorted_schema_files(config.DATABASE_SCHEMA_DIR)
    if upgrade_files:
        _log_debug("upgrade point: " + upgrade_files[0])
    _run_schema_files([os.path.join(config.DATABASE_SCHEMA_DIR, file_name) for file_name in upgrade_files])

def drop():
    db_name = config.database_connection.get("database")
    if not db_name:
        _log_error("no database name to drop")
        return False
    drop_command = "drop database if exists " + db_name + ";"
    return _execute_non_query(drop_command)

def create():
    _create_schema()
    _create_procedure()

def upgrade():
    _create_upgrade_schemas()
    _create_procedure()

def drop_and_create():
    if drop():
        create()
