#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
elif is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
elif is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
