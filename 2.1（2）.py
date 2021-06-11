class Teacher(object):
    display = "teacher"

    def __init__(self, name, age, course, salary):
        self.name = name
        self.age = age
        self.course = course
        self.__salary = salary

    def __str__(self, print_all=False):
        if print_all:
            return " ".join(str(item) for item in (
                self.display, self.name, self.age, self.course, self.__salary))
        else:
            return self.name


class Student(object):
    display = "student"

    def __init__(self, name, sid, classes, score):
        self.name = name
        self.sid = sid
        self.calssed = classes
        self.__score = score

    def __str__(self):
        return self.name


t1 = Teacher("Li", 35, "Python1", 30000)
s1 = Student('Wang', 18, "python2", "A")
print(t1)
print(s1)
print(t1.__str__())
print(t1.__str__(True))
