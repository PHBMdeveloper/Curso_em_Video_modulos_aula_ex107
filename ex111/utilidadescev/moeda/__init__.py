def moeda(n):
    return "R$" + ('%.2f' % n).replace('.', ',')


def metade(n, formato):
    if formato is True:
        resultado = n / 2
        return "R$" + ('%.2f' % resultado).replace('.', ',')
    else:
        return n / 2


def dobro(n, formato):
    if formato is True:
        resultado = n * 2
        return "R$" + ('%.2f' % resultado).replace('.', ',')
    else:
        return n * 2


def aumentar(n, per, formato):
    if formato is True:
        resultado = n + ((n / 100) * per)
        return ("R$" + ('%.2f' % resultado).replace('.', ','))
    else:
        return n + ((n / 100) * per)


def diminuir(n, per, formato):
    if formato is True:
        resultado = n - ((n / 100) * per)
        return ("R$" + ('%.2f' % resultado).replace('.', ','))
    else:
        return n - ((n / 100) * per)


def resumo(p, a, d):
    print('-'*30)
    print(' '*8 + 'RESUMO DO VALOR' + ' '*7)
    print('-'*30)
    print(f'Preço analizado:    {moeda(p)}')
    print(f'Dobro do preço:     {dobro(p, True)}')
    print(f'Metade do preço:    {metade(p, True)}')
    print(f'{a}% de aumento:     {aumentar(p, a, True)}')
    print(f'{d}% de redução:     {diminuir(p, d, True)}')
    print('-'*30)
