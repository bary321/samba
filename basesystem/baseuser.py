# coding:utf-8

from __future__ import unicode_literals

import commands

from jinja2 import Template

from logger import logger

__author__ = 'bary'
__metaclass__ = type

grep = r"cat /etc/passwd | grep '{{ user }}'"
addcmd = r"useradd -g {{ initgroup }} -M -s /bin/nologin {{ user }}"
addgroup = r"useradd -G {{ groupname }}"
delcmd = r"userdel {{ user }}"
passwd = r"passwd {{ user }}"
passwd1 = r"""echo "{{ password }}" | passwd --stdin {{ user }}"""
csh = r"usermod -s {{ shell }} {{ user }}"
cid = r"usermod -u {{ uid }} {{ user }}"
chome = r"usermod -d {{ home }} {{ user }}"
luser = r"passwd {{ user }} -l"
uuser = r"passwd {{ user }} -u"
error = r"A error arise when do cmd '{{ cmd }}': {{ status }}"

log = logger.getLogger('logger.baseuser')


def template(temp, **kwargs):
    templates = Template(temp)
    return templates.render(kwargs)


def docmd(temp, **kwargs):
    templates = Template(temp)
    cmd = templates.render(kwargs)
    err, status = commands.getstatusoutput(cmd)
    if err:
        message = template(error, cmd=cmd, status=status)
        log.error(message)
        return 1
    else:
        return 0


class BaseUser:
    """def __init__(self, name=""):
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

    def changepasswd(self, user=""):
        return docmd(passwd, user=user)

    def createuser(self, initgroup="", user=""):
        return docmd(addcmd, initgroup="", user=user)

    def deluser(self, user=""):
        return docmd(delcmd, user=user)

    def changepasswdnon(self, password="", user=""):
        return docmd(passwd1, password=password, user=user)

    def changehomedir(self, home="", user=""):
        return docmd(chome, home=home, user=user)

    def changeshell(self, shell="", user=""):
        return docmd(csh, shell=shell, user=user)

    def changeID(self, uid="", user=""):
        return docmd(cid, uid=uid, user=user)

    def addusertogroup(self, groupname=""):
        return docmd(addgroup, groupname=groupname)

    def userlock(self, user=""):
        return docmd(luser, user=user)

    def userunlock(self, user=""):
        return docmd(uuser, user=user)


if __name__ == "__main__":
    print template(luser, user="aaa")
    print docmd(luser, user="aaa")
