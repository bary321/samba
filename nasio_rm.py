#!/usr/local/bin/python2.7
# coding:utf-8
import argparse
from samba.operation import rm, add

__author__ = 'bary'

parser = argparse.ArgumentParser(prog="Nasio rm")
parser.add_argument("-u", "--user", help="the user name to be operated")
parser.add_argument("-d", "--dir", required=True, help="the directory name to be operated")
parser.add_argument("-v", "--valid", action="store_true", help="when del user from dir.weather del it"
                                                               "from the valid user list")
parser.add_argument("-w", "--write", action="store_true", help="when del user from dir.weather del it"
                                                               "from the write user list")
args = parser.parse_args()

temp = False
if args.dir and args.user:
    temp = True

if args.valid or args.write:
    if not temp:
        print "Error:the valid and write optional only used when options user and dir exist"
        exit()
if args.user:
    rm.rmuser(args.dir, args.user, valid=args.valid, write=args.write)
else:
    rm.rmdir(args.dir)

add.writetosmb()
