# coding:utf-8

# from __future__ import unicode_literals

import commands

import os

from samba.system.basesystem.baseuser import docmdtmp, template

from pprint import pprint

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger

log = logger.getLogger('logger.basedirectory')


def docmd(temp, **kwargs):
    return docmdtmp(log, temp, **kwargs)


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
getacl = r"getfacl -p {{ path }}"


class BaseDirectory:
    """
    this class is designed to finish the operation of system folder.
    """

    def __init__(self):
        pass

    def pathexist(self, path=""):
        cmd = template(info, path=path)
        err, status = commands.getstatusoutput(cmd)
        if err == 512:
            return False
        else:
            return True

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

    def chmod(self, u="", g="", o="", path=""):
        return docmd(chmod, u=u, g=g, o=o, path=path)

    def chgroup(self, groupname="", path=""):
        return docmd(groupname=groupname, path=path)

    def _aclinfo(self, path=""):
        cmd = template(getacl, path=path)
        d, t = commands.getstatusoutput(cmd)
        if d != 0:
            err = "a error arise when do cmd (" + cmd + ")" + " :\n" + t + " "
            log.error(err)
            return {}
        a = t.splitlines()
        temp = dict()
        temp["file"] = a[0].split(":")[1].strip(" ")
        temp["owner"] = a[1].split(":")[1].strip(" ")
        temp["owner's group"] = a[2].split(":")[1].strip(" ")
        temp["default mask"] = None
        temp["mask"] = None
        temp["default group"] = []
        temp["group"] = []
        temp["default user"] = []
        temp["user"] = []
        temp["default other"] = None
        temp["other"] = None
        for i in range(0, 3):
            del a[0]
        for e in a:
            f = e.split(":")
            g = False
            if f[0] == "default":
                g = True
                del f[0]
            if f[0] == "user":
                h = "user"
                del f[0]
            if f[0] == "group":
                h = "group"
                del f[0]
            if f[0] == "other":
                h = "other"
                del f[0]
            if f[0] == "mask":
                h = "mask"
                del f[0]
            if len(f[1].split("\t")) == 2:
                del f[1]
            if f[0] == "":
                if h == "user":
                    f[0] = temp["owner"]
                elif h == "mask":
                    if g:
                        temp["default mask"] = f[1]
                    else:
                        temp["mask"] = f[1]
                    continue
                elif h == "other":
                    if g:
                        temp["default other"] = f[1]
                    else:
                        temp["other"] = f[1]
                    continue
                else:
                    f[0] = temp["owner's group"]
            elif h == "user":
                if f[0] == temp["owner"]:
                    continue
            elif h == "group":
                if f[0] == temp["owner's group"]:
                    continue
            else:
                pass
            j = dict()
            j[f[0]] = f[1]
            if g:
                h = "default " + h
            temp[h].append(j)
        return temp

    def getacl(self, path):
        temp = self._aclinfo(path=path)
        for i in temp.keys():
            if not temp[i]:
                del temp[i]
        return temp

    def setaclgroup(self, group="", u="", path=""):
        return docmd(setaclg, group=group, u=u, path=path)

    def setacluser(self, user="", u="", path=""):
        return docmd(setaclu, group=user, u=u, path=path)

    def setumask(self, u="", path=""):
        return docmd(setaclm, u=u, path=path)

    def _getaclinfo(self, name="", path=""):
        temp = self.getacl(path=path)
        name_d = "default " + name
        tmp = {name: None, name_d: None}
        for i in temp.keys():
            if i == name:
                tmp[name] = temp[name]
            elif i == name_d:
                tmp[name_d] = temp[name_d]
            else:
                pass
        return tmp

    def getumask(self, path=""):
        return self._getaclinfo(name="mask", path=path)

    def aclgroup(self, path=""):
        return self._getaclinfo(name="group", path=path)

    def acluser(self, path=""):
        return self._getaclinfo(name="user", path=path)

    def aclother(self, path=""):
        return self._getaclinfo(name="other", path=path)

    def mkdir(self, path=""):
        return docmd(mkdir, path=path)

    def deldir(self, path=""):
        return docmd(rmdir, path=path)

    def __mvdir(self, path=""):
        pass

    def __mvdirnon(self, path=""):
        pass

    def __cpdir(self, path=""):
        pass


if __name__ == '__main__':
    a = BaseDirectory()
    pprint(a.getacl(path="/s"))
    pprint(a.getumask(path="/"))
    pprint(a.aclgroup(path="/"))
    pprint(a.acluser(path="/"))
    pprint(a.aclother(path="/"))
    print a.pathexist("/")
    print a.pathexist("/s")
