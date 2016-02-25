#!/usr/local/bin/python2.7
# coding:utf-8

import argparse
from samba.operation import add
__author__ = 'bary'

parser = argparse.ArgumentParser(prog="Nasio add")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--user", help="the user name for operation")
parser.add_argument("-d", "--dir", required=True, help="the user name for operation")
group.add_argument("-p", "--path", help="only used when option dir exist")
parser.add_argument("-v", "--valid", action="store_true", help="only used when option dir and user exist")
parser.add_argument("-w", "--write", action="store_true", help="only used when option dir and user exist")
args = parser.parse_args()
if args.path:
    add.adddir(dir=args.dir, path=args.path)
    add.writetosmb()
    exit()
if args.user:
    add.adduser(user=args.user, dire=args.dir, valid=args.valid, write=args.write)
    add.writetosmb()
    exit()




































































