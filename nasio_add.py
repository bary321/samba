# coding:utf-8
import argparse
__author__ = 'bary'


def addgrouptodir(group, v, w):
    pass

def addusertodir(user, v, w):
    pass

parser = argparse.ArgumentParser(prog="Nasio add")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-g", "--group", required=True, help="the user group for operation")
group1.add_argument("-u", "--user", required=True, help="the user for operation")
parser.add_argument("-v", "--valid", help="")
parser.add_argument("-w", "--write", help="")
args = parser.parse_args()
if args.group:
    addgrouptodir(args.group, args.v, args.w)
elif args.user:
    addusertodir(args.user, args.v, args.w)










































































