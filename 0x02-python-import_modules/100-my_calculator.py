#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as bag
    leg = len(bag)
    operator = add, sub, mul, div
    if leg > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(bag[1])
    b = int(bag[3])
    result = a + b
    if leg == 4:
        print(f"{a} {operator} {b} = {result}")
