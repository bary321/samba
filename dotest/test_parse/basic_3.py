# coding:utf-8
import argparse
__author__ = 'bary'


parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square",
                    type=int)
args = parser.parse_args()
print args.square**2














































































