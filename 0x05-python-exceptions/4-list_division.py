#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            result.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except ValueError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return (result)
