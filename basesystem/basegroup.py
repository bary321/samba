# coding:utf-8

from __future__ import unicode_literals

import os

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

log = logger.getLogger('logger.group')


class BaseGroup:
    def __init__(self, name=""):
        self.name = str(name)
        self.id = -1
        self.numbers = ""
        if self.name:
            self.__init()

    def __init(self):
        try:
            f = open(r"/etc/group")
            for line in f:
                line = line.rstrip(r"\n")
                attribute = line.split(r":")
                if self.name == attribute[0]:
                    self.id = int(attribute[2])
                    if attribute[3] == "\n":
                        self.numbers = ""
                    else:
                        self.numbers = attribute[3]
                    break
            f.close()
            return 0
        except Exception as e:
            error = "some error arise when get attribute of " + self.name + ":" + str(e)
            log.error(error)
            return -1

    def all(self):
        print {"group name": self.name,
               "group id": self.id,
               "group numbers": self.numbers
               }

    def groupexist(self):
        pass

    def delgroup(self):
        pass

    def creategroup(self):
        pass

    def addgroupdb(self):
        pass

    def changegroupID(self):
        pass

    def getgroupID(self):
        pass

    def getnumbers(self):
        pass

    def numberexist(self):
        pass

    def addnumbers(self):
        pass

    def delnumbers(self):
        pass
