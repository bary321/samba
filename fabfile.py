# coding:utf-8
import os
import logger
import commands
from fabric.api import local, lcd, cd, run ,env
__author__ = 'bary'

log = logger.getLogger("logger.fabfile")

env.hosts = ['root@192.168.2.90:22']
env.password = 'passwd'

def Hello():
    with cd("/"):
        run("ls")
    print commands.getstatusoutput("ls")


















































































