# coding:utf-8
import gc
__metaclass__ = type
__author__ = 'bary'


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if cls.cer:
            cls.cer = False
            return super(Singleton, cls).__new__(cls)
        else:
            raise TypeError('[%s] could be instantiated only once!' % cls.__name__)

    cer = True

    def __del__(self):
        self.__class__.cer = True


if __name__ == "__main__":
    a = Singleton()
    print a.__class__.cer

    del a
    print gc.collect()
    b = Singleton()
    print b
