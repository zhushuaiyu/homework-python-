import threading
import time


class Singleton(type):
    _instances = dict()
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            with Singleton._instance_lock:
                if cls not in cls._instances.keys():
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class OtherClass(object):
    def __new__(cls):
        return super(OtherClass, cls).__new__(cls)

    def __init__(self):
        self.a = 'a_default'
        super(OtherClass, self).__init__()


class MyClass(OtherClass, metaclass=Singleton):
    class_attribute = 'class_default'

    def __init__(self):
        time.sleep(1)
        super(MyClass, self).__init__()
        self.x = 'x_default'

    @classmethod
    def class_func(cls):
        print('class function')
