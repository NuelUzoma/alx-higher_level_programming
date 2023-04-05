#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers
Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm:
O(log(n)), O(n), O(nlog(n)) or O(n2)"""


def find_peak(list_of_integers):
    """The function definition to find the peak integer"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
