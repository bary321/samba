# coding:utf-8
from __future__ import unicode_literals

import commands
import re
import logging

__author__ = 'bary'

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('/var/log/samba/samba-admin.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
simple = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(simple)

logger.addHandler(fh)
logger.addHandler(ch)


def GetGroupname():
    err, status = commands.getstatusoutput(r"cat /etc/group | grep 'zexabox_*\|^admin'")
    if err != 0:
        error = "some error arise when getgroupname" + status
        logger.error(error)
        return err
    groupname = re.split('[\n]', status)
    group = []
    for i in groupname:
        group.append(re.split('[:]', i)[0])
    return group


def GroupAdd(name):
    if name in GetGroupname():
        warnings = "the group name '" + name + "' already exist"
        logger.warning(warnings)
        return 0
    cmd = r"groupadd " + name
    err, status = commands.getstatusoutput(cmd)
    if err != 0:
        error = "some error arise when add group:" + status
        logger.error(error)
        return err
    else:
        return 0


def GroupDel(name):
    if name not in GetGroupname():
        warnings = "the group name '" + name + "' does not exist"
        logger.warning(warnings)
        return 1
    cmd = r"groupdel " + name
    err, status = commands.getstatusoutput(cmd)
    if err != 0:
        error = "some error arise when del group:" + status
        logger.error(error)
        return err
    else:
        return 0


def UserAdd(name, groupname="", passwd=""):

    if groupname:
        if name not in GetGroupname():
            warnings = "the group name '" + name + "' does no exist"
            logger.warning(warnings)
            return 1
        cmd = r"useradd -M -g " + groupname + "-s /bin/nologin" + name
    else:
        cmd = r"useradd -M -s /bin/nologin " + name
    err, status = commands.getstatusoutput(cmd)
    if err != 0:
        error = "some error arise when add user:" + status
        logger.error(error)
        return err
    else:
        if passwd:
            cmd = r"echo " + passwd + "|" + r"smbpasswd -a " + name + "--stdin"
            err, status = commands.getstatusoutput(cmd)
            if err != 0:
                error = "some error arise when set smbpasswd for" + name + ": " + status
                logger.error(error)
                return err
        return 0




def GetGroupID(groupname):
    cmd = r"cat /etc/group | grep '" + groupname + "'"
    err, status = commands.getstatusoutput(cmd)
    if err != 0:
        error = "some error arise when getgroupname" + status
        logger.error(error)
        return err
    try:
        return re.split('[:]', status)[2]
    except TypeError as e:
        error = "A error arise when getgroupid : \n " + str(e)
        logger.error(error)
        return -1
    except IndexError as e:
        error = "A error arise when getgroupid : \n " + str(e)
        logger.error(error)
        return -1


def UserExist(username):
    cmd = r"cat /etc/passwd | grep '" + username + "'"
    err, status = commands.getstatusoutput(cmd)
    if status:
        return 0
    else:
        return 1

def GetUsersBG(groupname):
    groupID = GetGroupID(groupname)
    if groupID == -1:
        return -1
    else:
        cmd = r"cat /etc/passwd | grep '" + groupID + "'"
    err, status = commands.getstatusoutput(cmd)
    if err != 0:
        if not status:
            warnings = "can't find the " + groupname + "'s " + "numbers"
            logger.warning(warnings)
            return 0
        else:
            errors = "some error arise when get users with ID " + groupID + ": " + status
            logger.error(errors)
            return err
    usersname = re.split('[\n]', status)
    users = []
    for i in usersname:
        try:
            if int(re.split('[:]', i)[2]) == int(groupID):
                users.append(re.split('[:]', i)[0])
        except TypeError as e:
            info = "except TypeError when users : \n " + str(e)
            logger.info(info)
            return -1
        except IndexError as e:
            info = "except IndexError when users : \n " + str(e)
            logger.info(info)
            return -1
    return {groupname: users}


def Userdel(name):
    if not UserExist(name):
        warnings = "the user '" + "' doesn't exist"
        logger.warning(warnings)
        return 1
    cmd = r"userdel " + name
    err, status = commands.getstatusoutput(cmd)
    if err == 1536:
        warnings = status
        logger.warning(warnings)
        return 0
    elif err == 0:
        return 0
    else:
        error = "A error arise when del user " + name + ": " + status
        logger.error(error)
        return -1


if __name__ == "__main__":
    print GetGroupID("zexabox_admin")
    print GetGroupname()
    print GetUsersBG("root"), "GETUsers"
    print UserAdd(name='hjy'), "adduser"
    # print Userdel('hjy'), "userdel"
    print GroupAdd('hjy'), "groupadd"
    print GroupDel('hjy'), "groupdel"