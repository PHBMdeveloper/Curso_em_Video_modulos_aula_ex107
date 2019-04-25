def moeda(n):
    return "R$" + ('%.2f' % n).replace('.', ',')


def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, per):
    return n + ((n / 100) * per)


def diminuir(n, per):
    return n - ((n / 100) * per)
