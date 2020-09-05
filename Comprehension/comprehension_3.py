generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) #saida 0
print(next(generator)) #saida 4
print(next(generator)) #saida 14
print(next(generator)) #saida 36
print(next(generator)) #saida 64
#print(next(generator)) #erro na saida

#ele vai pegar apenas os numeros pares em um range de 0 a 9