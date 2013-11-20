#!/usr/bin/env python3

from . import log_service

class ServiceContext:

    def __init__(self):
        self._log_service = log_service.LogService()

    @property
    def log_service(self):
        return self._log_service

    @log_service.setter
    def log_service(self, log_service):
        self._log_service = log_service
