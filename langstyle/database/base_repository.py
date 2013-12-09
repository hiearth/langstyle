#!/usr/bin/env python

from mysql import connector as dbconnector
from .. import config

class BaseRepository:

    def _create_connection(self):
        return dbconnector.connect(**config.database_connection)

    def _log_error(self, error):
        config.service_factory.get_log_service().error(error.msg)

    def _call_proc_query_all(self, proc_name, proc_args):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            cursor.callproc(proc_name, proc_args)
            return self._fetch_all(cursor)
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.close()

    def _call_proc_query_one(self, proc_name, proc_args):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            cursor.callproc(proc_name, proc_args)
            return self._fetch_one(cursor)
        except dbconnector.DatabaseError as db_error:
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.close()
        return None

    def _call_proc_non_query(self, proc_name, proc_args):
        try:
            conn = self._create_connection()
            cursor = conn.cursor()
            result = cursor.callproc(proc_name,proc_args)
            conn.commit()
            return result
        except dbconnector.DatabaseError as db_error:
            conn.rollback()
            self._log_error(db_error)
        finally:
            cursor.close()
            conn.close()
        return None

    def _fetch_one(self,cursor):
        for result in cursor.stored_results():
            first_result = result.fetchone()
            if first_result:
                return first_result[0]
        return None

    def _fetch_all(self, cursor):
        all_results = []
        for result in cursor.stored_results():
            all_results.extend(result.fetchall())
        return all_results