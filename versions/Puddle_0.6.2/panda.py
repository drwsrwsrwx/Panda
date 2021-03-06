# Author  : @DivorcedRSAKey
# Purpose : This library was designed to keep me from rewriting all my code constantly
#           for different projects.
# Version : Puddle (0.6.2)

import sys
calling_file = sys.argv[0].split(".py")[0]

class Logger():
    def __init__(self, logFile="%s.plog" % calling_file, verbose=False, write=False, debug=True):
        self.strf = "[%Y-%M-%d %H:%M:%S]"
        self.types = {
            "error": "[!]",
            "info": "[-]",
            "plus": "[+]",
            "debug": "[D]",
            "warn": "[W]"
            }
        self.verbose = verbose
        self.write = write
        self.logFile = logFile

    def log(self, logMsg, logType='info', verbose=True, write=True, logFile=self.logFile):
        from time import strftime as s, gmtime as g
        log = "%s %s %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def success(self, logMsg, logType='plus', verbose=True, write=True, logFile=self.logFile):
        from time import strftime as s, gmtime as g
        log = "%s %s Error: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def error(self, logMsg, logType='error', verbose=True, write=True, logFile=self.logFile):
        from time import strftime as s, gmtime as g
        log = "%s %s Error: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def debug(self, logMsg, logType='debug', verbose=True, write=True, logFile=self.logFile):
        from time import strftime as s, gmtime as g
        log = "%s %s Debug: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def warning(self, logMsg, logType='warn', verbose=True, write=True, logFile=self.logFile):
        from time import strftime as s, gmtime as g
        log = "%s %s Warning: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(logFile, "a")
            lf.write(log+"\n")
            lf.close()

