#!/usr/bin/env python3
from math import pi
import sys
import errno


class TerminalColor:
    erro = '\033[91m'
    normal = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("é necessario informar a raio do circulo")
    print("Sintaxe: {} < raio >".format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.erro +
              'O raio deve ser um valor numerico' +
              TerminalColor.normal)
        sys.exit(errno.EINVAL)


raio = sys.argv[1]
area = circulo(raio)
print('Areá do circulo: ', area)
