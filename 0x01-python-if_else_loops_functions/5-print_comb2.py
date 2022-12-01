#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print("{}".format('0' + str(i) if i < 10 else i), end=", ")
