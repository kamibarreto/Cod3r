produto =  {'Nome': 'Caneta Chic', 'Preço': 14.99,
            'Importado': True, 'Estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor) #eles viram uma varivel com valores, quando atriubuidos a eles, e eles vão falar a ultima cadeia, ou seja:
#estoque 793