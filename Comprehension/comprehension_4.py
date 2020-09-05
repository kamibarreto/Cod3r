generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)

#ele vai pegar apenas os numeros pares em um range de 0 a 9
