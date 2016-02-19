# coding:utf-8
import argparse
__author__ = 'bary'


def showgroup(group):
    pass

def showuser(user):
    pass

def showall():
    pass

def showdir(dir):
    pass

def showcon():
    pass


parser = argparse.ArgumentParser(prog="Nasio list")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-g", "--group", default="", help="show Group's info or show all Group's")
group.add_argument("-u", "--user", default="", help="show User's info or show all User's")
group.add_argument("-a", "--all", action="store_true", help="show all info")
group.add_argument("-d", "--directory", default="", help="show Dir's info or show all Dir's")
group.add_argument("-c", "--configuration", default="", help="display the samba configuration file")
args = parser.parse_args()
if args.g:
    showgroup(args.g)
elif args.u:
    showuser(args.u)
elif args.a:
    showall()
elif args.c:
    showcon()
elif args.d:
    showdir(args.d)










































































