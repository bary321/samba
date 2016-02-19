# coding:utf-8
import argparse
__author__ = 'bary'


def rmgroupfromdir(group, f, i):
    pass

def rmuserfromdir(user, f, i):
    pass

def rmdir(dir, f, i):
    pass

parser = argparse.ArgumentParser(prog="Nasio rm")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-g", "--group", required=True, help="the user group for operation")
group1.add_argument("-u", "--user", required=True, help="the user for operation")
group1.add_argument("-d", "--dir", required=True, help="the directory for operation")
parser.add_argument("-f", "--force", action="store_true", help="")
parser.add_argument("-i", "--ignore", action="store_true", help="")
args = parser.parse_args()
if args.group:
    rmgroupfromdir(args.group, args.f, args.ignore)
elif args.user:
    rmuserfromdir(args.user, args.f, args.ignore)
elif args.dir:
    rmdir(args.dir, args.f, args.ignore)

















































































