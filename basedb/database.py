# coding:utf-8
import sqlite3

from jinja2 import Environment, FileSystemLoader, Template

import os

__author__ = 'bary'
__metaclass__ = type

if os.name == "nt":
    import logger
else:
    from samba import logger


log = logger.getLogger("logger.basedata")
if os.name == "nt":
    pathofdb = r"E:\workstation\samba\dbase.db3"
else:
    pathofdb = r"/home/ftp/samba/dbase.db3"
tableglobal = r"global"
tabledir = r"direct"


class BaseData(object):
    def __init__(self):
        self.con = sqlite3.connect(pathofdb)
        self.cur = self.con.cursor()

    def getallinfodir(self):
        cmd = r"SELECT * FROM " + tabledir
        temp = self.cur.execute(cmd)
        return temp.fetchall()

    def getalldire(self):
        alldir = [i[0] for i in self.getallinfodir()]
        return alldir

    def getglobalinfo(self):
        cmd = r"SELECT * FROM " + tableglobal
        temp = self.cur.execute(cmd)
        return temp.fetchall()

    def getall(self):
        env = Environment(loader=FileSystemLoader('templates'), auto_reload=True)
        template = env.get_template(r"smb.muban")
        return template.render(g=self.getglobalinfo()[0], dire=self.getallinfodir())

    def getvalidusers(self, dire=""):
        return [i[2] for i in self.getallinfodir() if i[0] == dire]

    def getwritelist(self, dire=""):
        return [i[9] for i in self.getallinfodir() if i[0] == dire]

    def getusers(self, dire=""):
        return {"valid users": self.getvalidusers(dire=dire)[0], "write user": self.getwritelist(dire=dire)[0]}

    def updatedatabase(self, table="", column="", dire="", info=""):
        try:
            cmd = "update " + table + " set " + column + " = '" + info + "' where name = '" + dire + "'"
            self.con.execute(cmd)
            self.con.commit()
            log.info(cmd)
            return 0
        except Exception as e:
            log.error(str(e))
            self.con.commit()
            return -1

    def changevalidusers(self, dire="", users=""):
        self.updatedatabase(table="direct", column="valid_users", dire=dire, info=users)
        self.con.commit()
        return 0

    def changewriteusers(self, dire="", lis=""):
        self.updatedatabase(table="direct", column="write_list", dire=dire, info=lis)
        self.con.commit()
        return 0

    def adddir(self, dire="", path="", valid_users="", write_list=""):
        if self.direxit(dire=dire):
            infos = "the directory name '" + dire + "' already exist."
            print infos
            return 1
        if dire and path:
            m = 4
        else:
            m = 0
        if valid_users:
            m += 2
        if write_list:
            m += 1
        if m < 4:
            print "no directory name or path input"
            return 1
        elif m == 4:
            templa = Template("INSERT INTO direct SELECT '{{ dire }}', '{{ path }}',valid_users,force_user,"
                              "force_group,read_only,create_mask,directory_mask,guest_ok,write_list FROM "
                              "direct WHERE name='tmp'")
            cmd = templa.render(dire=dire, path=path)
        elif m == 5:
            templa = Template("INSERT INTO direct SELECT '{{ dire }}', '{{ path }}',valid_users,force_user,"
                              "force_group,read_only,create_mask,directory_mask,guest_ok, '{{ write_list }}' FROM "
                              "direct WHERE name='tmp'")
            cmd = templa.render(dire=dire, path=path, write_list=write_list)
        elif m == 7:
            templa = Template("INSERT INTO direct SELECT '{{ dire }}', '{{ path }}','{{ valid_users }}',force_user,"
                              "force_group,read_only,create_mask,directory_mask,guest_ok,'{{ write_list }}' FROM "
                              "direct WHERE name='tmp'")
            cmd = templa.render(dire=dire, path=path, valid_users=valid_users, write_list=write_list)
        else:
            error = "? m error .value : " + str(m)
            log.error(error)
            return 0
        self.con.execute(cmd)
        self.con.commit()
        log.info(cmd)
        return 0

    def addvaliduser(self, dire="", user=""):
        if self.validuserexist(dire=dire, user=user):
            infos = "the user name '" + user + "' already exist in " + dire + "'s valid users"
            print infos
            return 1
        temp = self.getvalidusers(dire=dire)[0]
        if temp:
            users = str(temp) + "," + user
        else:
            users = user
        self.changevalidusers(dire=dire, users=users)
        self.con.commit()
        return 0

    def addwriteuser(self, dire="", user=""):
        if self.writelistexist(dire=dire, user=user):
            infos = "the user name '" + user + "' already exist in " + dire + "'s write list"
            print infos
            return 1
        temp = self.getwritelist(dire=dire)[0]
        if temp:
            lis = str(temp) + "," + user
        else:
            lis = user
        self.changewriteusers(dire=dire, lis=lis)
        self.con.commit()
        return 0

    def deldir(self, dire=""):
        if dire is None:
            cmd = "DELETE FROM " + tabledir + " WHERE name IS NULL"
            self.con.execute(cmd)
            self.con.commit()
            log.info(cmd)
            return 0
        if self.direxit(dire=dire):
            cmd = "DELETE FROM " + tabledir + " WHERE name = '" + dire + "'"
            print cmd
            print r"Are you sure to delete directory '" + dire + r"' ?(Y/y/yes/N/n/no)"
            judge = raw_input().lower()
            if judge == "yes" or judge == "y":
                self.con.execute(cmd)
                self.con.commit()
                log.info(cmd)
                return 0
            elif judge == "n" or judge == "no":
                return 1
            else:
                print "unrecognized input. exit"
                return 1
        else:
            print "no such directory"
            return 1

    def delvaliduser(self, user="", dire=""):
        if not self.validuserexist(dire=dire, user=user):
            inf = "the user name '" + user + "' don't exist in " + dire + "'s valid users"
            print inf
            return 1
        else:
            temp = self.getvalidusers(dire=dire)[0].strip(",").split(",")
            temp.remove(user)
            self.changevalidusers(dire=dire, users=",".join(temp))
            # print self.getvalidusers(dire=dire)[0].strip(",").split(",").remove(user)
            return 0

    def delwritelist(self, user="", dire=""):
        if not self.writelistexist(dire=dire, user=user):
            inf = "the user name '" + user + "' don't exist in " + dire + "'s write list"
            print inf
            return 1
        else:
            temp = self.getwritelist(dire=dire)[0].strip(",").split(",")
            temp.remove(user)
            self.changewriteusers(dire=dire, lis=",".join(temp))
            return 0

    def direxit(self, dire=""):
        if dire in self.getalldire():
            return True
        else:
            return False

    def validuserexist(self, dire="", user=""):
        # if user in self.getvalidusers(dire=dire)[0].strip(",").split(","):
        try:
            self.getvalidusers(dire=dire)[0].strip(",").split(",").index(user)
            return True
        except ValueError:
            return False

    def writelistexist(self, dire="", user=""):
        # if user in self.getwritelist(dire=dire)[0].strip(",").split(","):
        try:
            self.getwritelist(dire=dire)[0].strip(",").split(",").index(user)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    a = BaseData()
    # a.addvaliduser(dire="tmp", user="aaaa,bbbb")
    # a.addwriteuser(dire="tmp", user="a")
    print a.getwritelist(dire="tmp")
    a.delwritelist(user="a", dire="tmp")
    print a.getwritelist(dire="tmp")
    print a.writelistexist(dire="tmp", user="a")
    a.addwriteuser(dire="tmp", user="a")
    a.adddir("one", "/nas/")
