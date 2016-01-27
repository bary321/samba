# coding:utf-8
import logging
import os
from database import BaseData

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

log = logger.getLogger("logger.dirbase")


class DirBase(object):
    def __new__(cls, dire):
        if dire:
            if type(dire) != str:
                errors = "the type of directory name is wrong"
                raise TypeError(errors)
            obj = BaseData()
            if not obj.direxit(dire=dire):
                errors = "the directory name '" + dire + "' don't exist"
                raise NameError(errors)
            return object.__new__(cls)
        else:
            errors = "Name don't have value"
            raise ValueError(errors)

    def __init__(self, dire):
        self.obj = BaseData()
        self.name = dire

    def getalldir(self):
        return self.obj.getalldire()

    def getall(self):
        return self.obj.getusers(dire=self.name)

    def getvaliduser(self):
        return self.obj.getvalidusers(dire=self.name)

    def getwritelist(self):
        return self.obj.getwritelist(dire=self.name)

    def addvaliduser(self, user):
        return self.obj.addvaliduser(dire=self.name, user=user)

    def delvaliduser(self, user):
        return self.obj.delvaliduser(dire=self.name, user=user)

    def addwriteuser(self, user):
        return self.obj.addwriteuser(dire=self.name, user=user)

    def delwriteuser(self, user):
        return self.obj.delwritelist(dire=self.name, user=user)

    def validuserexist(self, user):
        return self.obj.validuserexist(dire=self.name, user=user)

    def writelistexit(self, user):
        return self.obj.writelistexist(dire=self.name, user=user)


if __name__ == "__main__":
    a = DirBase(dire="tmp")
    a.addvaliduser(user="aaaa")
    print a.getall()
    a.delvaliduser(user="545")
    a.delvaliduser(user="aaaa")
    print a.getvaliduser()
    a.addwriteuser(user="aaa")
    print a.getwritelist()
    a.delwriteuser(user="aaa")
    print a.getwritelist()
    b = DirBase(1)
