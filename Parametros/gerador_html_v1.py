#!/usr/bin/env python3
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    #Testes (Assertions)
    assert tag_bloco('Incluindo com sucesso!') == \
        '<div class="success">Incluindo com sucesso!</div>'

    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'

    print(tag_bloco('bloco'))