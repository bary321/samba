# coding:utf-8
import commands
__author__ = 'bary'

d, t = commands.getstatusoutput("getfacl /temp/test")
print t
