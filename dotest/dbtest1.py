# coding:utf-8
import sqlite3
import os

__author__ = 'bary'

conn = sqlite3.connect("E:\workstation\samba\mydatabase1.db3")
conn.isolation_level = None
info = "&"*20
conn.execute(
    "create table if not EXISTS t1(id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(128), info VARCHAR)")
conn.execute("insert into t1(name, info) VALUES('zhaowei', '%s')" % info)
conn.commit()
cur = conn.cursor()
cur.execute("select * from t1")
res = cur.fetchall()
print 'row:', cur.rowcount
print 'desc', cur.description
for line in res:
    for f in line:
        print f,
    print
print '-'*60
conn.execute("insert into t1(name, info) VALUES('zhaowei', 'only a test')")
cur.execute("select * from t1")
res = cur.fetchone()
print 'row:', cur.rowcount
for f in res:
    print f,
print
res = cur.fetchone()
print 'row:', cur.rowcount
for f in res:
    print f,
print
print "-"*60

cur.close()
conn.close()
os.remove("E:\workstation\samba\mydatabase1.db3")
