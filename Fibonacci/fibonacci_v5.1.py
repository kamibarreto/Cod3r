#!/usr/bin/env python3


#0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    resultado = [0, 1]
    print(f'{resultado[-2]}, {resultado[-1]}', end=',')
    while resultado[-1] < limite:
        proximo = sum(resultado)
        print(proximo, end=',')
        penultimo = resultado [-1]
        resultado[-2] = proximo 

if __name__ == "__main__":
    for fib in fibonacci(100):
        print(fib, end=',')
