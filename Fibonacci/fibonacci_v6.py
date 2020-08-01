#!/usr/bin/env python3


#0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break  #se o a quantidade de coisas na cadeia (len) for igual a quantidade ( vc atribui la em ccima) vai dar break, ou seja, vai para a proxima "linha"
    return resultado

if __name__ == "__main__":
    #listar os 20 primeiro numeros 
    for fibi in fibonacci(20):
        print(fibi, end=',')
