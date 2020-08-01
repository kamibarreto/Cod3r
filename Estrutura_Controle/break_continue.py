for x in range(1, 11):
    if x % 2 == 0:
        continue 
        #o continue ele interrompe a repetição e vai para a proxima
        #ele esta relacionado com o "for" 
    print(x)


for x in range(1, 11):
    if x == 5:
        break
        #ele continua fazendo a repetição ate conseguir encontrar o valor e ir para a proxima
        #teste e verá que quando chegar no 5, ele pula pro "fim" pq ele encontrou a setença 5  
    print(x)

print('FIM')