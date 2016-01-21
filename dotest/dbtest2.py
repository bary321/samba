# coding:utf-8
from __future__ import unicode_literals
import sqlite3
__author__ = 'bary'

con = sqlite3.connect(r"E:\workstation\samba\dbase.db3")
cur = con.cursor()
cur.execute(r"select * from dir")
a = cur.fetchall()

con.close()















































































