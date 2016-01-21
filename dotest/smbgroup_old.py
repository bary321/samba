# coding:utf-8
from __future__ import unicode_literals
import commands
import re
import logging

__author__ = 'bary'

logger = logging.getLogger("logger.smbgroup")


class Smbgroup(object):
    def __init__(self):
        self.all = []

    @classmethod
    def getallgroupname(self):
        err, status = commands.getstatusoutput(r"cat /etc/group | grep 'zexabox_*\|^admin'")
        if err != 0:
            if not status:
                warnings = "there's no group name like 'zexabox_*'"
                logger.warning(warnings)
                return 1
            else:
                error = "some error arise when get all group name" + status
                logger.error(error)
                return err
        groupname = re.split('[\n]', status)
        for i in groupname:
            self.all.append(re.split('[:]', i)[0])
        return self.all

    @classmethod
    def groupadd(self, name):
        if name in self.getallgroupname():
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

    @classmethod
    def groupdel(self, name):
        if name not in self.getallgroupname():
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

    @classmethod
    def getgroupid(self, groupname):
        cmd = r"cat /etc/group | grep '" + groupname + "'"
        err, status = commands.getstatusoutput(cmd)
        if err != 0:
            if not status:
                warnings = "can't find the group's id"
                logger.warning(warnings)
                return 1
            else:
                error = "some error arise when getgroupname" + status
                logger.error(error)
                return err
        try:
            return 0, re.split('[:]', status)[2]
        except TypeError as e:
            error = "A error arise when getgroupid : \n " + str(e)
            logger.error(error)
            return -1
        except IndexError as e:
            error = "A error arise when getgroupid : \n " + str(e)
            logger.error(error)
            return -1