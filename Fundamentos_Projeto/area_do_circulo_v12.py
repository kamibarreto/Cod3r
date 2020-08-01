#!/usr/bin/env python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("é necessario informar a raio do circulo")
    print("Sintaxe: {} < raio >".format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Areá do circulo: ', area)

#aq vc vai definir uma função help, para ajudar 