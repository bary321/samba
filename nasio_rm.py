# coding:utf-8
import argparse
__author__ = 'bary'


parser = argparse.ArgumentParser(prog="Nasio rm")
parser.add_argument("-u", "--user", help="the user name to be operated")
parser.add_argument("-d", "--dir", required=True, help="the directory name to be operated")
parser.add_argument("-v", "--valid", action="store_true", help="when del user from dir.weather del it"
                                                               "from the valid user list")
parser.add_argument("-w", "--write", action="store_true", help="when del user from dir.weather del it"
                                                               "from the write user list")
args = parser.parse_args()

















































































