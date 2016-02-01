# coding:utf-8

# from __future__ import unicode_literals

import commands

import os

from samba.system.basesystem.baseuser import docmd, template

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

log = logger.getLogger('logger.basedirection')

info = r"ls -ld {{ path }}"
chgrp = r"chgrp -R {{ groupname }} {{ path }}"
chown = r"chown -R {{ username }} {{ path }}"
chmod = r"chmod -R {% if u == "" %} u={{ u }} {% endif %}{%if g == "" %} g={{ g }} {% endif %}\
{% if o == "" %} o={{ o }} {% endif %} {{ path }}"
mkdir = r"mkdir -p {{ path }}"
rmdir = r"rmdir -pdf {{ path }}"
setaclu = r"setfacl -Rd -m u:{{ user }}:{{ u }} {{ path }}"
setaclo = r"setfacl -Rd -m u::{{ u }} {{ path }}"
setaclg = r"setfacl -Rd -m g:{{ group }}:{{ u }} {{ path }}"
setaclm = r"setfacl -Rd -m m:{{ u }} {{ path }}"
getacl = r"getfacl {{ path }}"


class BaseDirection:
    """
    this class is designed to complete the operation of the system folder.
    """

    def __init__(self):
        pass

    def _getinfo(self, path):
        cmd = template(info, path=path)
        err, att = commands.getstatusoutput(cmd)
        if err != 0:
            error = "A error arise go get '" + path + "' info"
            log.error(error)
            return {"path": path,
                    "jurisdiction": "",
                    "hardlinkorsub": "",
                    "owner": "",
                    "group": "",
                    "size": "",
                    "changetime": "",
                    }
        att = att.split(" ")
        if "d" not in att[0]:
            warning = "the path you input is not a direction"
            log.warning(warning)
            return {"path": path,
                    "jurisdiction": "",
                    "hardlinkorsub": "",
                    "owner": "",
                    "group": "",
                    "size": "",
                    "changetime": "",
                    }
        try:
            jurisdiction = att[0]
            hardlinkorsub = int(att[1])
            owner = att[2]
            group = att[3]
            size = int(att[4])
            if att[6] == "":
                changetime = (att[5], att[7], att[8])
            else:
                changetime = (att[5], att[6], att[7])
            print att[8]
        except Exception as e:
            error = "A error arise when get attribute of dir " + path + str(e)
            log.error(error)
            return {"path": path,
                    "jurisdiction": "",
                    "hardlinkorsub": "",
                    "owner": "",
                    "group": "",
                    "size": "",
                    "changetime": "",
                    }
        return {"path": path,
                "jurisdiction": jurisdiction,
                "hardlinkorsub": hardlinkorsub,
                "owner": owner,
                "group": group,
                "size": size,
                "changetime": changetime
                }

    def getall(self, path=""):
        print self._getinfo(path=path)

    def changejurisdiction(self, u="", g="", o="", path=""):
        return docmd(chmod, u=u, g=g, o=o, path=path)

    def __createsub(self):
        pass

    def chmod(self, u="", g="", o="", path=""):
        return docmd(chmod, u=u, g=g, o=o, path=path)
        pass

    def chgroup(self, groupname="", path=""):
        return docmd(groupname=groupname, path=path)

    def _aclinfo(self):
        pass

    def getacl(self, path):
        return docmd(getacl, path=path)

    def setaclgroup(self, group="", u="", path=""):
        return docmd(setaclg, group=group, u=u, path=path)

    def setacluser(self, user="", u="", path=""):
        return docmd(setaclu, group=user, u=u, path=path)

    def setumask(self, u="", path=""):
        return docmd(setaclm, u=u, path=path)

    def getumask(self, path=""):
        pass

    def aclgroup(self, path=""):
        pass

    def acluser(self, path=""):
        pass

    def mkdir(self, path=""):
        return docmd(mkdir, path=path)

    def deldir(self, path=""):
        return docmd(rmdir, path=path)

    def mvdir(self, path=""):
        pass

    def mvdirnon(self, path=""):
        pass

    def cpdir(self, path=""):
        pass


if __name__ == '__main__':
    a = BaseDirection()
    a.mkdir(path=r"/temp/test")
    a.getall(path=r"/temp/test")
    a.setaclgroup(group="root", u="rwx", path=r"/temp/test")
    a.setacluser(user="root", u="rwx", path=r"/temp/test")
