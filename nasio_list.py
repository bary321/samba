#!/usr/local/bin/python2.7
# coding:utf-8

import argparse
from operation import list
from pprint import pprint

__author__ = 'bary'


def showgroup(group):
    if type(group) == bool:
        if group:
            pprint(list.getgroup())
        return 0
    pprint(list.getgroup(group))


def showuser(user):
    if type(user) == bool:
        if user:
            pprint(list.getuser())
        return 0
    pprint(list.getuser(user))


def showcon():
    print(list.all())


def showdir(dir):
    if type(dir) == bool:
        if dir:
            pprint(list.getdir())
        return 0
    pprint(list.getdir(dir))


parser = argparse.ArgumentParser(prog="Nasio list")
parser.add_argument("-a", "--all", help="show all group or user or dir or configuration",
                    choices=["user", "dir", "con"],
                    metavar="( group | user | dir | con )")
group = parser.add_mutually_exclusive_group(required=False)
# group.add_argument("-g", "--group", help="show Group's info")
group.add_argument("-u", "--user", help="show User's info")
# group.add_argument("--all", help="show all info")
group.add_argument("-d", "--dir", help="show Dir's info")
# group.add_argument("--config", action="store_true", help="display the samba configuration file")
args = parser.parse_args()
# print args
if args.all:
    if args.user or args.dir:
        print "Don't mix '--all' and other option"
        exit()
    if args.all == "user":
        showuser(True)
    elif args.all == "dir":
        showdir(True)
    elif args.all == "con":
        showcon()

else:
    if args.user:
        showuser(args.user)
    # elif args.all:
    #     showall()
    # elif args.config:
    #     showcon()
    elif args.dir:
        showdir(args.dir)
