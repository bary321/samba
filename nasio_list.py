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
group = parser.add_mutually_exclusive_group()
group.add_argument("-g", "--group")
group.add_argument("-u", "--user")
group.add_argument("-a", "--all")
group.add_argument("-d", "--directory")
group.add_argument("-c", "--configuration")
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










































































