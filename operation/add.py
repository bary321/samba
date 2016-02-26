# coding:utf-8
import list
from samba.basedb import database
from samba.basedb.dirbase import DirBase
from samba.system.user import User
from samba.system.group import Group
from samba.system.directory import Directory

__author__ = 'bary'

data = database.BaseData()


def adddir(dir, path):
    """
    path should be test.In jurisdiction.
    """
    if data.direxit(dir):
        print "Error:this directory named %s already exist." % dir
    else:
        D = Directory(path)
        if D.pathexist(path):
            data.adddir(dire=dir, path=path)
        else:
            print "Error:this path '%s' don't exist." % path


def adduser(user, dire, valid=True, write=False):
    if not data.direxit(dire):
        print "Error:the directory named %s doesn't exist." % dire
    else:
        U = User(user)
        if not U.userexist():
            y = raw_input("user %s don't exist.create now?(Y/y)" % user)
            y.lower()
            if y == "y":
                g = raw_input("create with user name or other?(input noting or existed group)")
                if g:
                    G = Group(g)
                    if G.groupexist():
                        U.createuser(initgroup=g, user=user)
                        p = raw_input("Input passwd:(default is the user name)")
                        if not p:
                            U.changepasswdnon("%s" % user)
                        else:
                            U.changepasswdnon(p)
                    else:
                        print "Error:the group named %s don't exist.quit" % g
                else:
                    G = Group(user)
                    if G.groupexist():
                        print "Error:Can't create group '%s'.It already exist." % user
                    else:
                        G.creategroup()
                        U.createuser(initgroup=user, user=user)
                        p = raw_input("Input passwd:(default is the user name)")
                        if not p:
                            U.changepasswdnon("%s" % user)
                        else:
                            U.changepasswdnon(p)
                adduser(user, dire, valid=valid, write=write)
            else:
                exit()
        else:
            Dir = DirBase(dire)
            if valid:
                if Dir.validuserexist(user):
                    print "Error:the user '%s' already exist in this directory's valid user list" % user
                else:
                    Dir.addvaliduser(user)
            if write:
                if Dir.writelistexit(user):
                    print "Error:the user '%s' already exist in this directory's write user list" % user
                else:
                    Dir.addwriteuser(user)


def writetosmb():
    return data.writetosmb()


if __name__ == "__main__":
    adddir('tp', '/home/tp')
    adduser("adasd", "tmp", write=True)
