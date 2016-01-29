# coding:utf-8
import logging
import os
#???
__author__ = 'bary'
if os.name == "nt":
    filepath = r"E:\workstation\samba\test.log"
else:
    filepath = r"/home/ftp/samba/test.log"
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(filepath)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
simple = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(simple)

logger.addHandler(fh)
logger.addHandler(ch)


def getLogger(name):
    return logging.getLogger(name)
