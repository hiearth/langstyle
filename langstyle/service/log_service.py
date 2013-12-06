#!/usr/bin/env python

class LogService:

    def info(self, msg):
        pass

    def debug(self, msg):
        pass
    
    def warn(self, msg):
        pass

    def error(self, msg):
        self._print("ERROR", msg)

    def fatal(self, msg):
        pass

    def _print(self, log_level, msg):
        print(log_level + ": " + msg)