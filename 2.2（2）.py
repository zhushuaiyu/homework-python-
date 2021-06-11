import threading
import time


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            with Singleton._instance_lock:
                if self._instance is None:
                    self._instance = self._cls(*args, **kwargs)
        return self._instance


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
