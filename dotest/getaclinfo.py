# coding:utf-8
import pprint
import commands

__author__ = 'bary'

d, t = commands.getstatusoutput("getfacl -p /temp/test")
a = t.splitlines()
temp = dict()
temp["file"] = a[0].split(":")[1].strip(" ")
temp["owner"] = a[1].split(":")[1].strip(" ")
temp["owner's group"] = a[2].split(":")[1].strip(" ")
temp["default mask"] = None
temp["mask"] = None
temp["default group"] = []
temp["group"] = []
temp["default user"] = []
temp["user"] = []
temp["default other"] = None
temp["other"] = None

for i in range(0,3):
    del a[0]
for e in a:
    f = e.split(":")
    g = False
    if f[0] == "default":
        g = True
        del f[0]
    if f[0] == "user":
        h = "user"
        del f[0]
    if f[0] == "group":
        h = "group"
        del f[0]
    if f[0] == "other":
        h = "other"
        del f[0]
    if f[0] == "mask":
        h = "mask"
        del f[0]
    if len(f[1].split("\t")) == 2:
        del f[1]
    if f[0] == "":
        if h == "user":
            f[0] = temp["owner"]
        elif h == "mask":
            if g:
                temp["default mask"] = f[1]
            else:
                temp["mask"] = f[1]
            continue
        elif h == "other":
            if g:
                temp["default other"] = f[1]
            else:
                temp["other"] = f[1]
            continue
        else:
            f[0] = temp["owner's group"]
    elif h == "user":
        if f[0] == temp["owner"]:
            continue
    elif h == "group":
        if f[0] == temp["owner's group"]:
            continue
    else:
        pass
    j = dict()
    j[f[0]] = f[1]
    if g:
        h = "default " + h
    temp[h].append(j)

pprint.pprint(temp)




























































