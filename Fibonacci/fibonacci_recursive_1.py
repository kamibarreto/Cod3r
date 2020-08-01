#!/usr/bin/env python3
def fibonacci(quantidade, sequencia=(0,1)):
    #Condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)