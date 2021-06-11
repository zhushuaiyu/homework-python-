import threading
import time


def Singleton(cls):
    _instance = None
    _instance_lock = threading.Lock()

    def _wrapper(*args, **kargs):
        nonlocal _instance
        if _instance is None:
            with _instance_lock:
                if _instance is None:
                    _instance = cls(*args, **kargs)
        return _instance

    return _wrapper


class OtherClass(object):
    def __new__(cls):
        return super(OtherClass, cls).__new__(cls)

    def __init__(self):
        self.a = 'a_default'
        super(OtherClass, self).__init__()


@Singleton
class MyClass(OtherClass):
    class_attribute = 'class_default'

    def __init__(self):
        time.sleep(1)
        super(__class__, self).__init__()
        self.x = 'x_default'

    @classmethod
    def class_func(cls):
        print('class function')
