#!/usr/bin/env python3

from math import pi


def circulo(raio):
    return pi * raio ** 2 #return vai retonar o valor para a variavel a baixo, "area"



if __name__ == '__main__': 
    raio = float(input('Informe o raio: '))
    area = circulo(raio)
    print('Areá do circulo: {:.2f}'.format(area))

#quando vc usa o >>> import area_do_circulo_v9 as v9<<<< vc esta transoformando aquilo tudo em apenas "v9"
'''>>> v9.circulo(21.3)
1425.3091710071535
>>> area = v9.circulo(21.3)
>>> area
1425.3091710071535
>>> area * 2
2850.618342014307'''

#exemplos acima