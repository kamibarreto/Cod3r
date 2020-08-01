#!/usr/bin/env python3
from math import pi


def circulo(raio):
    print(f'Area do circulo é : {pi * raio ** 2:.2f}')



if __name__ == '__main__': 
    raio = float(input('Informe o raio: '))
    circulo(raio)


#esse exemplo aq eu usei o "def" para meio que transformar o arquivo v8 em uma biblioteca, e defini (def) o circulo como a area
