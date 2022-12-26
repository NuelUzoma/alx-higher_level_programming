#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == None):
        return (None)
    for i in range(len(sentence)):
        return (len(sentence), sentence[0])
