#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max_int = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return (max_int)
