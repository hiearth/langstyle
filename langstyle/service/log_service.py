#!/usr/bin/env python

class LogService:

    def info(self, msg):
        self._print("INFO", msg)

    def debug(self, msg):
        self._print("DEBUG", msg)
    
    def warn(self, msg):
        self._print("WARN", msg)

    def error(self, msg):
        self._print("ERROR", msg)

    def fatal(self, msg):
        self._print("FATAL", msg)

    def _print(self, log_level, msg):
        print(log_level + ": " + msg)