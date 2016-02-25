# coding:utf-8

from __future__ import unicode_literals

import os

from samba.system.basesystem.baseuser import template, docmdtmp

import commands

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

log = logger.getLogger('logger.group')


def docmd(temp, **kwargs):
    return docmdtmp(log, temp, **kwargs)


grep = r"cat /etc/group | grep '{{ group }}'"
adduser = r"gpasswd -a {{ user }} {{ group }}"
deluser = r"gpasswd -d {{ user }} {{ group }}"
addg = r"groupadd {{ group }}"
delg = r"groupdel {{ group }}"
gpasswdM = r"gpasswd -M {{ user }} {{ group }}"


class BaseGroup:
    """
    有一个问题：我的cmd是从user抓过来的，那log的名称会变成user的吗？会有问题，但已解决
"""

    def __init__(self):
        pass

    def groupexist(self, group=""):
        cmd = template(grep, group=group)
        err, status = commands.getstatusoutput(cmd)
        if status:
            return True
        else:
            return False

    def _groupinfo(self, group=""):
        try:
            f = open(r"/etc/group")
            for line in f:
                line = line.rstrip(r"\n")
                attribute = line.split(r":")
                if group == attribute[0]:
                    id = attribute[2]
                    if attribute[3] == "\n":
                        numbers = ""
                    else:
                        numbers = attribute[3].strip("\n")
                    f.close()
                    return {"name": group,
                            "id": id,
                            "numbers": numbers
                            }
            return {"name": '',
                    "id": "",
                    "numbers": ""}
        except Exception as e:
            error = "some error arise when get attribute of " + group + ":" + str(e)
            log.error(error)
            return {"name": '',
                    "id": "",
                    "numbers": ""}

    def groupinfo(self, group=""):
        if os.name == "nt":
            return {}
        print self._groupinfo(group=group)

    def delgroup(self, group=""):
        return docmd(delg, group=group)

    def creategroup(self, group=""):
        return docmd(addg, group=group)

    def addgroupdb(self):
        pass

    def getgroupID(self, group=""):
        return self._groupinfo(group=group)["id"]

    def getnumbers(self, group=""):
        ID = self.getgroupID(group=group)
        num_id = self.getnumberbyid(ID)
        try:
            temp = self._groupinfo(group=group)["numbers"].split(",")
            if temp[0] != "":
                temp.extend(num_id)
                return temp
            else:
                return num_id
        except TypeError:
            return self.getnumberbyid(ID)

    def getnumberbyid(self, id=""):
        if id:
            f = open(r"/etc/passwd")
            temp = []
            for line in f:
                attribute = line.split(r":")
                if id == attribute[3]:
                    temp.append(attribute[0].strip("\n"))
            return temp

    def numberexist(self, group="", user=""):
        if user in self.getnumbers(group=group):
            return True
        else:
            return False

    def addnumbers(self, user="", group=""):
        return docmd(adduser, user=user, group=group)

    def delnumbers(self, user="", group=""):
        return docmd(deluser, user=user, group=group)


if __name__ == "__main__":
    a = BaseGroup()
    """print "create group:", a.creategroup(group="tmp")
    print "group exist:", a.groupexist(group="tmp")
    print "groupinfo:", a.groupinfo(group="tmp")
    print "get 'tmp' ID:", a.getgroupID(group="tmp")
    print "get numbers of 'tmp':", a.getnumbers(group="tmp")
    print "add numbers :", a.addnumbers(user="temp", group="tmp")
    print "get numbers of 'tmp':", a.getnumbers(group="tmp")
    print "number exist:", a.numberexist(group="tmp", user="temp")
    print "del numbers:", a.delnumbers(user="temp", group="tmp")
    print "number exist:", a.numberexist(group="tmp", user="temp")
    print "delgroup:", a.delgroup(group="tmp")
    print "group exist", a.groupexist(group="tmp")
    print "groupinfo", a.groupinfo(group="tmp")
"""
    print a.getnumbers("admin")
