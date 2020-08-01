#!/usr/bin/env python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2
# return vai retonar o valor para a variavel a baixo, "area"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("é necessario informar a raio do circulo")
        print("Sintaxe: {} < raio >".format(sys.argv[0][2:]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Areá do circulo: ', area)


#sys.arqv = o nome do arquivo, neste caso é a area do circulo v11
#ali em cima no segundo "if" pergunta se a menos de 2 cadeias no sys.arqv, se vc não inserir o valor, vai haver menos de 2 cadeias
