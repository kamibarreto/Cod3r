#Operador de membro

n = [1, 2, 3, "carla", "ana"]
print(2 in n)
print(2 not in n)
print("ana" in n)
#fica tipo, ana tem em "n"

print("=" * 40)
#operador de identidade

x = 3
y = x
z = 3
print(x is 3)
print(x is 4)
print(x is y)
print(x is not 4)
#fica tipo, x é 3, ou x é y

print('=' * 40)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)# são as mesma listas, true
print(lista_b is lista_c)# são listas diferentes, mesmo possuindo o mesmo conteudo
print(lista_a is not lista_c)# não é a mesma lista, ent True

