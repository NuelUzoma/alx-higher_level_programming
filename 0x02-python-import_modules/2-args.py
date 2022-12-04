#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as a
    leng = len(a)
    if leng == 1:
        print("0 arguments.")
    elif leng == 2:
        print(f"1 argument:\n1: {a[1]}")
    elif leng == 3:
        print(f"2 arguments:\n1: {a[1]}\n2: {a[2]}")
    elif leng == 4:
        print(f"3 arguments:\n1: {a[1]}\n2: {a[2]}\n3: {a[3]}")
    elif leng == 5:
        print(f"4 arguments:\n1:{a[1]}\n2:{a[2]}\n3:{a[3]}\n4:{a[4]}")
