# coding:utf-8
import argparse
__author__ = 'bary'


def showgroup(group):
    print "show group ", group
    pass

def showuser(user):
    print "show user ", user
    pass

def showall():
    print "show all "
    pass

def showdir(dir):
    print "show dir", dir
    pass

def showcon():
    print "show con"
    pass


parser = argparse.ArgumentParser(prog="Nasio list")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-g", "--group", default="", help="show Group's info or show all Group's")
group.add_argument("-u", "--user", default="", help="show User's info or show all User's")
group.add_argument("-a", "--all", action="store_true", help="show all info")
group.add_argument("-d", "--directory", default="", help="show Dir's info or show all Dir's")
group.add_argument("-c", "--configuration", action="store_true", default="", help="display the samba configuration file")
args = parser.parse_args()
print args
if args.group:
    showgroup(args.group)
elif args.user:
    showuser(args.user)
elif args.all:
    showall()
elif args.configuration:
    showcon()
elif args.directory:
    showdir(args.d)










































































