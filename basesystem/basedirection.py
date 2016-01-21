# coding:utf-8

from __future__ import unicode_literals
import commands
import logger

__author__ = 'bary'
__metaclass__ = type

log = logger.getLogger('logger.basedirection')
log.error("test")


class BaseDirection:
    def __init__(self, path=""):
        self.path = str(path)
        self.jurisdiction = ""
        self.hardlinkorsub = 0
        self.owner = ""
        self.group = ""
        self.size = 0
        self.changetime = ""
        if path:
            self.__init()

    def __init(self):
        cmd = r"ls -ld --full-time " + self.path
        err, att = commands.getstatusoutput(cmd)
        if err != 0:
            error = "A error arise go get '" + self.path + "' info"
            log.error(error)
            return -1
        att = att.split(" ")
        if "d" not in att[0]:
            warning = "the path you input is not a direction"
            log.warning(warning)
            return -1
        try:
            self.jurisdiction = att[0]
            self.hardlinkorsub = int(att[1])
            self.owner = att[2]
            self.group = att[3]
            self.size = int(att[4])
            self.changetime = (att[5], att[6], att[7])
        except Exception as e:
            error = "A error arise when get attribute of dir " + self.path + str(e)
            log.error(error)
            return -1
        return 0
