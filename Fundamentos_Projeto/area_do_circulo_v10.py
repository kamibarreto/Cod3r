#!/usr/bin/env python3
from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2 
#return vai retonar o valor para a variavel a baixo, "area"



if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Areá do circulo: ', area)

