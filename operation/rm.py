# coding:utf-8
from samba.basedb import dirbase
from samba.basedb import database

__author__ = 'bary'


def rmdir(dire):
    try:
        Data = dirbase.DirBase(dire)
        Data.deldir()
    except NameError:
        print "Error the directory name %s don't exist" % dire
        exit()


def rmuser(dire, user, valid=False, write=False):
    Data = database.BaseData()
    if not Data.direxit(dire):
        print "Error:the directory named %s doesn't exist." % dire
    else:
        if valid:
            if Data.validuserexist(dire=dire, user=user):
                Data.delvaliduser(dire=dire, user=user)
            else:
                print "Warning:user %s doesn't exist in %s's valid user list" % (user, dire)
        if write:
            if Data.writelistexist(dire=dire, user=user):
                Data.delwritelist(dire=dire, user=user)
            else:
                print "Warning:user %s doesn't exist in %s write list" % (user, dire)


if __name__ == "__main__":
    rmuser("tmp", "c")
