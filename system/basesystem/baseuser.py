# coding:utf-8

from __future__ import unicode_literals

import commands

from jinja2 import Template

import os

import sys

from platform import platform

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

reload(sys)

sys.setdefaultencoding('utf8')


def definesys():
    """
    distinguish which platform the program run with.
    """
    t = platform()
    if "centos" in t.split("-"):
        return 0
    elif "Ubuntu" or "debian" in t.split('-'):
        return 1
    elif "Windows" in t.split('-'):
        return -1
    else:
        raise SystemError("unrecognized system %s" % platform())


grep = r"cat /etc/passwd | grep '^{{ user }}:'"


def difaddcmd():
    if definesys() == 0:
        return r"useradd -g {{ initgroup }} -M -s /usr/sbin/nologin {{ user }}"
    elif definesys() == 1:
        return r"useradd -g {{ initgroup }} -M -s /bin/false {{ user }}"


def difaddcmddefault():
    if definesys() == 0:
        return r"useradd -M -s /usr/sbin/nologin {{ user }}"
    elif definesys() == 1:
        return r"useradd -M -s /bin/false {{ user }}"


addcmd = difaddcmd()
addcmddefault = difaddcmddefault()
addgroup = r"usermod -G {{ groupname }} {{ user }}"
delcmd = r"userdel {{ user }}"
# passwd = r"smbpasswd {{ user }}"
# passwd1 = r"""echo "{{ user }}:{{ password }}" | chpasswd"""
passwd = r"echo {{ user }} echo {{ user }} | smbpasswd -a -s {{ user }}"
passwd1 = r"echo {{ password }} echo {{ password }} | smbpasswd -a -s {{ user }}"
csh = r"usermod -s {{ shell }} {{ user }}"
cid = r"usermod -u {{ uid }} {{ user }}"
chome = r"usermod -d {{ home }} {{ user }}"
luser = r"passwd {{ user }} -l"
uuser = r"passwd {{ user }} -u -f"
error = r"A error arise when do cmd '{{ cmd }}': {{ status }}"
groups = "groups {{ user }}"

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
    this object design to operate users.
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
            """Attention: return a direction is better than a integer"""
            return {"name": "",
                    "id": "",
                    "group id": "",
                    "commet": "",
                    "home dir": "",
                    "shell": ""
                    }

    def userinfo(self, user=""):
        """
        why i use print here? Shouldn't this be return?
        -------
        change to return
        """
        if os.name == "nt":
            return {}
        return self.__userinfo(user=user)

    def changepasswd(self, user=""):
        return docmd(passwd, user=user)

    def changepasswdnon(self, password="", user=""):
        return docmd(passwd1, password=password, user=user)

    def createuser(self, initgroup="", user=""):
        return docmd(addcmd, initgroup=initgroup, user=user)

    def createuserdef(self, user=""):
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

    def showgroups(self, user=""):
        cmd = template(groups, user=user)
        err, status = commands.getstatusoutput(cmd)
        if err != 0:
            error = "A error arise when execute cmd(" + cmd + "):" + status
            log.error(error)
            return []
        return status.split(":")[1].strip(" ").split(" ")


if __name__ == "__main__":
    a = BaseUser()
    print template(grep, user="tmp")
    print "user='tmp' exist", a.userexist(user="tmp")
    print a.userinfo(user="tmp")
    print a.createuserdef(user="tmp")
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
    print a.createuserdef("tmmp"), "createuserdef"
    print a.changepasswd("tmmp")
    print a.deluser("tmmp")
