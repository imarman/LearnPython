a = 1
b = "abc"
print(type(1))  # <class 'int'>
print(type(int))  # <class 'type'>
print(type(b))  # <class 'str'>
print(type(str))  # <class 'type'>


# type -> int ->1
# type -> class ->obj

# object 是最顶层基类
# type 也是一个类，同时 type 也是一个对象

class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()
print(type(stu))  # <class '__main__.Student'>
print(type(Student))  # <class 'type'>
print(int.__bases__)  # (<class 'object'>,)
print(str.__bases__)  # (<class 'object'>,)
print(Student.__bases__)  # (<class 'object'>,)
print(MyStudent.__bases__)  # (<class '__main__.Student'>,)
print(type.__bases__)  # (<class 'object'>,)
print(object.__bases__)  # ()
print(type(object))  # <class 'type'>
