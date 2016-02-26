# coding:utf-8
from basesystem import baseuser

__author__ = 'bary'


class User(baseuser.BaseUser):
    def __init__(self, name=""):
        super(User, self).__init__()
        self.name = name

    def userexist(self):
        return super(User, self).userexist(self.name)

    def userinfo(self):
        return super(User, self).userinfo(self.name)

    def changepasswd(self):
        return super(User, self).changepasswd(self.name)

    def changepasswdnon(self, password=""):
        return super(User, self).changepasswdnon(password=password, user=self.name)

    def createuser(self, initgroup="", user=""):
        return super(User, self).createuser(initgroup=initgroup, user=user)

    def createuserdef(self):
        return super(User, self).createuserdef(self.name)

    def deluser(self):
        return super(User, self).deluser(user=self.name)

    def changehomedir(self, home=""):
        return super(User, self).changehomedir(home=home, user=self.name)

    def changeshell(self, shell=""):
        return super(User, self).changeshell(shell=shell, user=self.name)

    def changeID(self, uid=""):
        return super(User, self).changeID(uid=uid, user=self.name)

    def userlock(self):
        return super(User, self).userlock(user=self.name)

    def userunlock(self):
        return super(User, self).userunlock(user=self.name)

    def showgroups(self):
        return super(User, self).showgroups(user=self.name)

if __name__ == "__main__":
    a = User("tmp")
    print a.userexist()
    print a.userinfo()
    a.userunlock()
