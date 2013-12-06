#!/usr/bin/env python

from mysql import connector as dbconnector
from .. import config

class BaseRepository:

    def _create_connection(self):
        return dbconnector.connect(**config.database_connection)

    def _log_error(self, error):
        config.service_factory.get_log_service().error(error.msg)
