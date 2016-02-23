# coding:utf-8
from samba.basedb import database
from samba.system.group import Group
from samba.system.user import User
from samba import logger
from pprint import pprint
__author__ = 'bary'
__metaclass__ = type

"""this file will user to get all the information we need used in argparse module.
The data is very messy, but you can fix it out.Believe yourself and just do it."""

log = logger.getLogger("logger.getinfo")

temp = database.BaseData()


def allvname():
    vname = {}
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
    return vname


def allwname():
    wname = {}
    for i in temp.getalldire():
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
    return wname

def alluser():
    user = {}
    t = allvname().keys()
    t.extend(allwname().keys())
    t = list(set(t))
    for i in t:
        user[i] = {}
        try:
            user[i]["valid user"] = allvname()[i]
        except KeyError:
            pass
        try:
            user[i]["write list"] = allwname()[i]
        except KeyError:
            pass
    return user


def allgroups():
    group = {}
    t = allvname().keys()
    t.extend(allwname().keys())
    t = list(set(t))
    for i in t:
        tmp = User(i)
        if tmp.userexist():
            for j in tmp.showgroups():
                tp = Group(j)
                if tp.groupexist():
                    for k in tp.getnumbers():
                        try:
                            if k in group[j]:
                                continue
                            group[j].append(k)
                        except KeyError:
                            group[j] = []
                            group[j].append(k)
                else:
                    w = "the group " + j + " doesn't exist in system."
                    log.warning(w)
                    continue
        else:
            # w = "the user " + i + " doesn't exist in system."
            # log.warning(w)
            continue
    return group


def alldir():
    directory = {}
    for i in temp.getalldire():
        try:
            directory[i] = temp.getusers(i)
        except KeyError:
            directory[i] = None
            directory[i] = temp.getusers(i)
    return directory


def show_dir(dir=""):
    if not dir:
        print alldir()
        return 0
    try:
        print alldir()[dir]
        return 0
    except KeyError:
        print "It doesn't exist in configuration."
        return 1

def show_user(user=""):
    if not user:
        print alluser()
        return 0
    try:
        print alluser()[user]
        return 0
    except KeyError:
        print "It doesn't exist in configuration"
        return 1

def show_gruop(group=""):
    temp = {}
    if not group:
        temp = allgroups()
    else:
        try:
            temp = {group: allgroups()[group]}
        except KeyError:
            print "the group you inputed doesn't exist in configuration."
            return 1
        pass
    return temp


pprint(allgroups())































































