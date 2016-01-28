# coding:utf-8
__author__ = 'bary'


class One(object):
    def __init__(self):
        pass

    def pri(self, a):
        print [i for i in range(1, a)]


class Two(One):
    def __init__(self):
        super(Two, self).__init__()
        pass

    def pri(self, a):
        super(Two, self).pri(a)


if __name__ == '__main__':
    a = Two()
    a.pri(1)
