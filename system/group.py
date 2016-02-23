# coding:utf-8
from samba.system.basesystem import basegroup

__author__ = 'bary'


class Group(basegroup.BaseGroup):
    def __init__(self, name=""):
        super(Group, self).__init__()
        self.name = name

    def groupexist(self):
        return super(Group, self).groupexist(group=self.name)

    def groupinfo(self):
        return super(Group, self).groupinfo(group=self.name)

    def delgroup(self):
        return super(Group, self).delgroup(group=self.name)

    def creategroup(self):
        return super(Group, self).creategroup(group=self.name)

    def getgroupID(self):
        return super(Group, self).getgroupID(group=self.name)

    def getnumbers(self):
        """
        this method are different between the others.because there an unexpected error arise:
        File "/root/PycharmProjects/samba/system/basesystem/basegroup.py", line 94, in getnumbers
        ID = self.getgroupID(group=group)
        TypeError: getgroupID() got an unexpected keyword argument 'group'
        """
        # return super(Group, self).getnumbers(group=self.name)
        temp = basegroup.BaseGroup()
        return temp.getnumbers(group=self.name)

    def numberexist(self, user=""):
        return super(Group, self).numberexist(group=self.name, user=user)

    def addnumbers(self, user=""):
        return super(Group, self).addnumbers(user=user, group=self.name)

    def delnumbers(self, user=""):
        return super(Group, self).delnumbers(user=user, group=self.name)


if __name__ == "__main__":
    t = Group("c")
    print t.groupexist()
    print t.getgroupID()
    print t.getnumbers()
