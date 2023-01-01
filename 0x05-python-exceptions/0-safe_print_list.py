#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    try:
        while elements < x:
            print(my_list[elements], end='')
            elements += 1
    except IndexError:
        pass
    print()
    return (elements)
