def faixa_etaria(idade):
    if 0 <= idade < 18: #if idade in range(0, 17)
        return 'Menor de idade'
    elif idade in range(18, 65):#se quer que vá ate 64, coloque 65, sempre 1 a mais
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centanario'
    else:
        return 'Idade invalida'

    
if __name__ == '__main__':
        for idade in (17, 35, 87, 113, -2):
            print(f'{idade}: {faixa_etaria(idade)}')

