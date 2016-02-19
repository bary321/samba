# coding:utf-8

from __future__ import unicode_literals

import commands

from jinja2 import Template

import os

import sys

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

reload(sys)

sys.setdefaultencoding('utf8')

grep = r"cat /etc/passwd | grep '{{ user }}'"
addcmd = r"useradd -g {{ initgroup }} -M -s /sbin/nologin {{ user }}"
addcmddefault = r"useradd -M -s /usr/sbin/nologin {{ user }}"
addgroup = r"useradd -G {{ groupname }} {{ user }}"
delcmd = r"userdel {{ user }}"
passwd = r"passwd {{ user }}"
passwd1 = r"""echo "{{ user }}:{{ password }}" | chpasswd"""
csh = r"usermod -s {{ shell }} {{ user }}"
cid = r"usermod -u {{ uid }} {{ user }}"
chome = r"usermod -d {{ home }} {{ user }}"
luser = r"passwd {{ user }} -l"
uuser = r"passwd {{ user }} -u -f"
error = r"A error arise when do cmd '{{ cmd }}': {{ status }}"

log = logger.getLogger('logger.baseuser')


def template(tmp, **kwargs):
    templates = Template(tmp)
    return templates.render(kwargs)


def docmdtmp(loge, tmp, **kwargs):
    """
    find a bug when this function named docmd.The log name will always "logger.baseuser".Because
    i directly use docmd in other module. The logger inside function remain is logger.baseuser.So
    i write another function to customize the logger inside function.
    当这个函数直接叫docmd时出现了一个bug。当我直接在其他模块中调用这个函数时，Logger的名字总是baseuser。
    所以我写了另一个函数来定制Logger的名字
    """
    templates = Template(tmp)
    cmd = templates.render(kwargs)
    if os.name == "nt":
        print cmd
        return 0
    else:
        err, status = commands.getstatusoutput(cmd)
        if err:
            message = template(error, cmd=cmd, status=status)
            loge.error(message)
            return 1
        else:
            return 0


def docmd(tmp, **kwargs):
    return docmdtmp(log, tmp, **kwargs)


class BaseUser:
    """
    this object design to
"""

    def __init__(self):
        pass

    def userexist(self, user=""):
        cmd = template(grep, user=user)
        err, status = commands.getstatusoutput(cmd)
        if status:
            return True
        else:
            return False

    def __userinfo(self, user=""):
        try:
            f = open(r"/etc/passwd")
            for line in f:
                attribute = line.split(r":")
                if user == attribute[0]:
                    id = attribute[2]
                    initgroup = attribute[3]
                    commet = attribute[4]
                    home = attribute[5]
                    shell = attribute[6].rstrip("\n")
                    f.close()
                    return {"name": user,
                            "id": id,
                            "group id": initgroup,
                            "commet": commet,
                            "home dir": home,
                            "shell": shell
                            }
            return {"name": "",
                    "id": "",
                    "group id": "",
                    "commet": "",
                    "home dir": "",
                    "shell": ""
                    }
        except Exception as e:
            error = "some error arise when init basesystem user name of " + user + ": " + str(e)
            log.error(error)
            return 1

    def userinfo(self, user=""):
        if os.name == "nt":
            return {}
        print self.__userinfo(user=user)

    def changepasswd(self, user=""):
        return docmd(passwd, user=user)

    def changepasswdnon(self, password="", user=""):
        return docmd(passwd1, password=password, user=user)

    def createuser(self, initgroup="", user=""):
        return docmd(addcmd, initgroup=initgroup, user=user)

    def cuserdef(self, user=""):
        return docmd(addcmddefault, user=user)

    def deluser(self, user=""):
        return docmd(delcmd, user=user)

    def changehomedir(self, home="", user=""):
        return docmd(chome, home=home, user=user)

    def changeshell(self, shell="", user=""):
        return docmd(csh, shell=shell, user=user)

    def changeID(self, uid="", user=""):
        return docmd(cid, uid=uid, user=user)

    # def addusertogroup(self, groupname="", user=""):
    #    return docmd(addgroup, groupname=groupname, user=user)

    def userlock(self, user=""):
        return docmd(luser, user=user)

    def userunlock(self, user=""):
        return docmd(uuser, user=user)


if __name__ == "__main__":
    a = BaseUser()
    print template(grep, user="tmp")
    print "user='tmp' exist", a.userexist(user="tmp")
    print a.userinfo(user="tmp")
    print a.cuserdef(user="tmp")
    print "user='tmp' exist", a.userexist(user="tmp")
    print a.changehomedir(home="/home/tmp", user="tmp"), "changedir"
    print a.userinfo(user="tmp")
    print a.changeshell(shell="/bin/sh", user="tmp"), "changeshell"
    print a.userinfo(user="tmp")
    print a.changeID(uid="9999", user="tmp"), "change id"
    print a.userinfo(user="tmp")
    # print a.addusertogroup(groupname="temp", user="tmp"), "add user to group"
    print a.userlock(user="tmp"), "lock user"
    print a.userinfo(user="tmp")
    print a.userunlock(user="tmp"), "ulock user"
    print a.userinfo(user="tmp")
    print a.deluser(user="tmp"), "del user"
    print "user='tmp' exist", a.userexist(user="tmp")
