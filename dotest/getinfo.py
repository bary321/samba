# coding:utf-8
from samba.basedb import database
__author__ = 'bary'

"""this file will user to get all the information we need used in argparse module.
The data is very messy, but you can fix it out.Believe yourself and just do it."""


def line():
    print "*************************************"

temp = database.BaseData()
temp.getall()
line()
temp.getalldire()
line()
temp.getallinfodir()
line()

for i in temp.getalldire():
    print i
    print temp.getusers(i)
    print "******************"
















































































