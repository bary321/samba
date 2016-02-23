# coding:utf-8
from samba.basedb import database
from samba.system.group import Group
from samba.system.user import User
from samba import logger
from commands import getstatusoutput
__author__ = 'bary'

"""this file will user to get all the information we need used in argparse module.
The data is very messy, but you can fix it out.Believe yourself and just do it."""

log = logger.getLogger("logger.getinfo")
vname = {}
wname = {}
group = {}
temp = database.BaseData()
for i in temp.getalldire():
    for j in temp.getvalidusers(i):
        if not j:
            continue
        else:
            for k in j.split(","):
                k = k.strip(" ")
                try:
                    vname[k].append(i)
                except KeyError:
                    vname[k] = []
                    vname[k].append(i)
    for j in temp.getwritelist(i):
        if not j:
            continue
        else:
            for k in j.split(","):
                k = k.strip(" ")
                try:
                    wname[k].append(i)
                except KeyError:
                    wname[k] = []
                    wname[k].append(i)

for i in vname.keys():
    tmp = User(i)
    if tmp.userexist():
        for j in tmp.showgroups():
            tp = Group(j)
            if tp.groupexist():
                print tp.getnumbers()
            else:
                w = "the group " + j + " doesn't exist."
                log.warning(w)
                continue
    else:
        w = "the user " + i + " doesn't exist."
        log.warning(w)
        continue
















































































