#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv)
    if leng == 1:
        print("0 arguments.")
    if leng == 2:
        print(f"1 argument:\n1: {argv[1]}")
    if leng > 2:
        print(f"{leng} arguments:\n1: {argv[1]}\n2: {argv[2]}\n3: {argv[3]}\n4: {argv[4]}\n5: {argv[5]}\n6: {argv[6]}\n7: {argv[7]}\n8: {argv[8]}")
