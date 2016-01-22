# coding:utf-8

from __future__ import unicode_literals
import logger

__author__ = 'bary'
__metaclass__ = type

log = logger.getLogger('logger.baseuser')


class BaseUser:
    def __init__(self, name=""):
        self.name = str(name)
        self.id = -1
        self.initgroup = -1
        self.commet = ""
        self.home = ""
        self.shell = ""
        if self.name:
            self.__init()

    def __init(self):
        try:
            f = open(r"/etc/passwd")
            for line in f:
                attribute = line.split(r":")
                if self.name == attribute[0]:
                    self.id = int(attribute[2])
                    self.initgroup = int(attribute[3])
                    self.commet = attribute[4]
                    self.home = attribute[5]
                    self.shell = attribute[6].rstrip("\n")
                    break
            f.close()
            return 0
        except Exception as e:
            error = "some error arise when init basesystem user name of " + self.name + ": " + str(e)
            log.error(error)
            return -1

    def all(self):
        print {"user name": self.name,
               "user id": self.id,
               "user init group's id": self.initgroup,
               "user commet": self.commet,
               "user home direction": self.home,
               "user shell": self.shell
               }

    def userexist(self):
        pass

    def changeinitgroup(self):
        pass

    def changepasswd(self):
        pass

    def createuser(self):
        pass

    def deluser(self):
        pass

    def initpasswd(self):
        pass

    def changehomedir(self):
        pass

    def changeshell(self):
        pass

    def changecommet(self):
        pass

    def changeID(self):
        pass

    def add(self):
        pass


if __name__ == "__main__":
    a = BaseUser()
