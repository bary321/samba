# coding:utf-8
import getinfo
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
        print "Error:this directory already exist."
    else:
        D = Directory(path)
        if D.pathexist(path):
            data.adddir(dire=dir, path=path)
        else:
            print "Error:this path don't exist."


def adduser(user, dire, valid=True, write=False):
    if not data.direxit(dire):
        print "Error:the directory doesn't exist."
    else:
        U = User(user)
        if not U.userexist():
            y = raw_input("user %s don't exist.create now?(Y/y)" % user)
            y.lower()
            if y == "y":
                g = raw_input("create with user name or other?\n(input noting or existed group)")
                if g:
                    G = Group(g)
                    if G.groupexist():
                        U.createuser(initgroup=g, user=user)
                    else:
                        print "Error:group don't exist.quit"
            else:
                exit()
        else:
            Dir = DirBase(dire)
            if valid:
                if Dir.validuserexist(user):
                    print "Error:the user already exist in this directory's valid user list"
                else:
                    Dir.addvaliduser(user)
            if write:
                if Dir.writelistexit(user):
                    print "Error:the user already exist in this directory's write user list"
                else:
                    Dir.addwriteuser(user)


if __name__ == "__main__":
    adddir('tp', '/home/tp')
    adduser("adasd", "tmp", write=True)
