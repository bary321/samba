# coding:utf-8
from samba.system.basesystem.basedirectory import BaseDirectory
from samba import logger

__author__ = 'bary'

log = logger.getLogger("logger.directory")


class Directory(BaseDirectory):
    def __init__(self, path=""):
        super(Directory, self).__init__()
        self.path = path

    def pathexist(self, path=""):
        return super(Directory, self).pathexist(path=self.path)

    def changepath(self, path=""):
        self.path = path
        return 0

    def getall(self, path=""):
        return super(Directory, self).getall(self.path)

    def changejurisdiction(self, u="", g="", o="", path=""):
        return super(Directory, self).changejurisdiction(u=u, g=g, o=o, path=self.path)

    def chmod(self, u="", g="", o="", path=""):
        return super(Directory, self).chmod(u=u, g=g, o=o, path=self.path)

    def chgroup(self, groupname="", path=""):
        return super(Directory, self).chgroup(groupname=groupname, path=self.path)

    def getacl(self, path=""):
        return super(Directory, self).getacl(path=self.path)

    def setaclgroup(self, group="", u="", path=""):
        return super(Directory, self).setaclgroup(group=group, u=u, path=self.path)

    def setacluser(self, user="", u="", path=""):
        return super(Directory, self).setacluser(user=user, u=u, path=self.path)

    def setumask(self, u="", path=""):
        return super(Directory, self).setumask(u=u, path=self.path)

    def getumask(self, path=""):
        return super(Directory, self).getumask(path=self.path)

    def aclgroup(self, path=""):
        return super(Directory, self).aclgroup(path=self.path)

    def acluser(self, path=""):
        return super(Directory, self).acluser(path=self.path)

    def aclother(self, path=""):
        return super(Directory, self).aclother(path=self.path)

    def mkdir(self, path=""):
        return super(Directory, self).mkdir(path=self.path)

    def deldir(self, path=""):
        return super(Directory, self).deldir(path=self.path)
