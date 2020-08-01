b = 7.5
print(b.is_integer()) # pergunta se b é um numero inteiro

print(int.__add__(1, 3)) # igual a 1 + 3

print((-2).__abs__())# função interna do int, transforma o numero em positivo
print(abs(-2))

from decimal import Decimal, getcontext #vai ajudar com numero do tipo 9.2398103821

getcontext().prec =  4 #  aq vc escolhe quantas casas decimais quer ter na resposta da divisão
print(Decimal(1) / Decimal(7))

#como ver qual numero é maior usando o import decimal:

print(Decimal.max(Decimal(1), Decimal(7))) # aq mostra quem é o numero maior 
print(Decimal.min(Decimal(1), Decimal(7))) # aq mostra o menor numero 

