# coding:utf-8
from __future__ import unicode_literals
import sqlite3
import os

__author__ = 'bary'

try:
    con = sqlite3.connect("E:\workstation\samba\db.db3")
    globalkey = {r"dos charset": r"cp936",
                 r"server string": r"%h server (Samba, Ubuntu)",
                 r"map to guest": r"Bad User",
                 r"obey pam restrictions": r"Yes",
                 r"pam password change": "Yes",
                 r"passwd program": r"/usr/bin/passwd",
                 r"passwd chat": r"*Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %    n\n *password\supdated\ssuccessfully* .",
                 r"unix password sync": r"Yes",
                 r"syslog": 0,
                 r"log file": r"/var/log/samba/log.%m",
                 r"max log size": 1000,
                 r"dns proxy": r"No",
                 r"usershare allow guests": r"Yes",
                 r"panic action": r"/usr/share/samba/panic-action %d",
                 r"idmap config * : backend": r"tdb",
                 }
    con.execute(r"CREATE TABLE IF NOT EXISTS global(id INTEGER PRIMARY KEY ,dos_charset VARCHAR, server_string VARCHAR,"
                r"map_to_guest VARCHAR,obey_pam_restrictions VARCHAR, pam_password_change VARCHAR,"
                r"passwd_program VARCHAR, passwd_chat VARCHAR, unix_password_sync VARCHAR, "
                r"syslog varchar, log_file VARCHAR, max_log_size varchar, dns_proxy VARCHAR, usershare_allow_guests VARCHAR"
                r", panic_action VARCHAR, idmap_config VARCHAR)")
    con.commit()
    con.execute(r"INSERT INTO global(dos_charset, server_string,"
                r"map_to_guest,obey_pam_restrictions, pam_password_change,"
                r"passwd_program, passwd_chat, unix_password_sync, "
                r"syslog, log_file, max_log_size, dns_proxy, usershare_allow_guests"
                r", panic_action, idmap_config)VALUES ('cp936','%h server (Samba, Ubuntu)', 'Bad User','Yes','Yes','/usr/bin/passwd'," \
                r"'*Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %    n\n *password\supdated\ssuccessfully* .','Yes','0','/var/log/samba/log.%m'," \
                r"'1000', 'No', 'Yes', '/usr/share/samba/panic-action %d', 'tdb')")
    con.commit()
    cur = con.cursor()
    cur.execute("SELECT * FROM global")
    print cur.fetchall()
    con.execute(r"CREATE TABLE IF NOT EXISTS dir(name VARCHAR PRIMARY KEY ,path VARCHAR,"
                r"valid_users VARCHAR,"
                r"force_user VARCHAR,"
                r"force_group VARCHAR,"
                r"read_only VARCHAR,"
                r"create_mask VARCHAR,"
                r"directory_mask VARCHAR,"
                r"guest_ok VARCHAR,"
                r"write_list VARCHAR)")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok)VALUES ('admin', '/nas/admin','admin',"
                r"'nobody','nogroup','No','0777','0777','Yes')")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('public', '/nas/public',NULL ,"
                r"'nobody','nogroup','No','0777','0777','Yes', 'oem, public, admin')")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('repos', '/nas/repos',NULL ,"
                r"'nobody','nogroup','No','0777','0777','Yes', 'admin')")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('release', '/nas/public',NULL ,"
                r"'nobody','nogroup','No','0777','0777','Yes', 'admin')")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('tmp', '/nas/tmp',NULL ,"
                r"'nobody','nogroup','No','0777','0777','Yes', NULL )")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('oem', '/nas/tmp','oem, admin' ,"
                r"'nobody','nogroup','No','0777','0777','Yes', NULL )")
    con.commit()
    con.execute(r"INSERT INTO dir(name,path,valid_users,force_user"
                r",force_group,read_only,create_mask,directory_mask,"
                r"guest_ok, write_list)VALUES ('work', '/nas/work',NULL ,"
                r"'nobody','nogroup','No','0777','0777','Yes', NULL )")
    con.commit()
    for i in cur.fetchall():
        print i
        print
    cur.execute(r"select * from dir")
    print cur.fetchall()
    cur.close()
    con.close()
finally:
    os.remove(r"E:/workstations/samba/db.db3")
    pass
