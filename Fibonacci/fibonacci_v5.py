#!/usr/bin/env python3


#0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacc(limi):
    resulta = [0, 1]
    while resulta[-1] < limi:
        resulta.append(sum(resulta[-2:]))
    return resulta

if __name__ == "__main__":
    for fibi in fibonacc(100):
        print(fibi, end=',')
