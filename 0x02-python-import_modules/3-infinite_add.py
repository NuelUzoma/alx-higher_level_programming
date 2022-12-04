#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as a
    leg = len(a)
    if leg == 1:
        print('0')
    elif leg == 2:
        print(a[1])
    elif leg == 3:
        print(int(a[1]) + int(a[2]))
    elif leg == 4:
        print(int(a[1]) + int(a[2]) + int(a[3]))
    elif leg == 5:
        print(int(a[1]) + int(a[2]) + int(a[3]) + int(a[4]))
    elif leg == 7:
        print(int(a[1]) + int(a[2]) + int(a[3]) + int(a[4])+int(a[5])+int(a[6]))
