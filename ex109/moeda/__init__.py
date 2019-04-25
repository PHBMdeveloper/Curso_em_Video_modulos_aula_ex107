def moeda(n):
    return "R$" + ('%.2f' % n).replace('.', ',')


def metade(n, formato):
    if formato is True:
        return "R$" + ('%.2f' % n).replace('.', ',')
    else:
        return n / 2


def dobro(n, formato):
    if formato is True:
        return "R$" + ('%.2f' % n).replace('.', ',')
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
