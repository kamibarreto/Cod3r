PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica') #constantes tem que ser letras maiuscula
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos: #texto vai percorrer essa lista
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui uma palavra proibida', palavra)
            found = True
            break
    
    if not found:
        print('Texto autorizado:', texto)


