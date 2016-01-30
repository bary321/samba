# coding:utf-8

from __future__ import unicode_literals

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
mkdir = r"mkdir {{ path }}"
setaclu = r"setfacl -mRd u:{{ user }}:{{ u }} {{ path }}"
setaclo = r"setfacl -mRd u::{{ u }} {{ path }}"
setaclg = r"setfacl -mRd g:{{ group }}:{{ u }} {{ path }}"
setaclm = r"setfacl -mRd m:{{ u }} {{ path }}"
getacl = r"getfacl {{ path }}"


class BaseDirection:
    """
    def __init__(self, path=""):
        self.path = str(path)
        self.jurisdiction = ""
        self.hardlinkorsub = 0
        self.owner = ""
        self.group = ""
        self.size = 0
        self.changetime = ""
        if path:
            self.__init()

    def __init(self):
        cmd = r"ls -ld --full-time " + self.path
        err, att = commands.getstatusoutput(cmd)
        if err != 0:
            error = "A error arise go get '" + self.path + "' info"
            log.error(error)
            return -1
        att = att.split(" ")
        if "d" not in att[0]:
            warning = "the path you input is not a direction"
            log.warning(warning)
            return -1
        try:
            self.jurisdiction = att[0]
            self.hardlinkorsub = int(att[1])
            self.owner = att[2]
            self.group = att[3]
            self.size = int(att[4])
            self.changetime = (att[5], att[6], att[7])
        except Exception as e:
            error = "A error arise when get attribute of dir " + self.path + str(e)
            log.error(error)
            return -1
        return 0
        """

    def __init__(self):
        pass

    def _getinfo(self, path):
        cmd = template(info, path=path)
        err, att = commands.getstatusoutput(cmd)
        if err != 0:
            error = "A error arise go get '" + path + "' info"
            log.error(error)
            return {"jurisdiction": "",
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
            return {"jurisdiction": "",
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
            changetime = (att[5], att[6], att[7])
        except Exception as e:
            error = "A error arise when get attribute of dir " + path + str(e)
            log.error(error)
            return {"jurisdiction": "",
                    "hardlinkorsub": "",
                    "owner": "",
                    "group": "",
                    "size": "",
                    "changetime": "",
                    }
        return {"jurisdiction": jurisdiction,
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

    def createsub(self):
        pass

    def chmod(self):
        pass

    def chgroup(self):
        pass

    def getacl(self):
        pass

    def setacl(self):
        pass

    def setaclgroup(self):
        pass

    def setacluser(self):
        pass

    def setumask(self):
        pass

    def getumask(self):
        pass

    def aclexist(self):
        pass

    def aclgroup(self, groupname):
        pass

    def acluser(self, user):
        pass

    def deldir(self):
        pass

    def mvdir(self):
        pass

    def cpdir(self):
        pass
