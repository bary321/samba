# coding:utf-8
from __future__ import unicode_literals
from jinja2 import FileSystemLoader, Environment
import sqlite3

__author__ = 'bary'


def writetosmb():
    con = sqlite3.connect(r"E:\workstation\samba\dbase.db3")
    cur = con.cursor()
    cur.execute(r"SELECT * FROM global")
    globalkey = cur.fetchall()
    cur.execute(r"SELECT * FROM direct")
    dirmap = cur.fetchall()
    con.close()
    env = Environment(loader=FileSystemLoader('templates'), auto_reload=True)
    template = env.get_template(r"smb.muban")
    f = open("E:\workstation\samba\smb.conf", r"w")
    f.write(template.render(g=globalkey[0], dire=dirmap))
    f.close()


if __name__ == "__main__":
    writetosmb()
