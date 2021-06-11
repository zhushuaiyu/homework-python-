class Teacher(object):
    display = "teacher"

    def __init__(self, name, age, course, salary):
        self.name = name
        self.age = age
        self.course = course
        self.__salary = salary


class Student(object):
    display = "student"

    def __init__(self, name, sid, classes, score):
        self.name = name
        self.sid = sid
        self.calssed = classes
        self.__score = score


def print_obj(obj):
    print(obj.__dict__)


t1 = Teacher("Li", 35, "Python1", 30000)
s1 = Student('Wang', 18, "python2", "A")
print_obj(t1)
print_obj(s1)
