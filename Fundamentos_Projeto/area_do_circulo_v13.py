#!/usr/bin/env python3
from math import pi
import sys
#import errno

def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("é necessario informar a raio do circulo")
    print("Sintaxe: {} < raio >".format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        #sys.exit(1) ou sys.exit(errno.EPERM)
        #ele vai fechar o codigo se não houver o raio, ai ele acaba aq, se não ele pula para parte seguindo, tirei o else para testar ele 
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Areá do circulo: ', area)

#aq vc vai definir uma função help, para ajudar 