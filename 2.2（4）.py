import threading
import time


class Singleton(object):
    _instance = dict()
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton._instance.keys():
            with Singleton._instance_lock:
                if cls not in Singleton._instance.keys():
                    Singleton._instance[cls] = super(Singleton, cls).__new__(cls)
                    Singleton._instance[cls]._intialed = False
        return Singleton._instance[cls]


class OtherClass(object):
    def __new__(cls):
        return super(OtherClass, cls).__new__(cls)

    def __init__(self):
        self.a = 'a_default'
        super(OtherClass, self).__init__()


class MyClass(Singleton, OtherClass):
    class_attribute = 'class_default'

    def __init__(self):
        if not self._initialed:
            with self._instance_lock:
                if not self._initialed:
                    super(MyClass, self).__init__()
                    time.sleep(1)
                    self.x = 'x_default'
                    self._initialed = True

    @classmethod
    def class_func(cls):
        print('class function')
