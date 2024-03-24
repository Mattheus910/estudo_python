def metade(n=0, formato=False):
    res = n - (n / 2)
    return res if not formato else formatacao(res)

def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else formatacao(res)

def aumento(n=0, taxa=0, formato=False):
    res = n + ((taxa / 100) * n)
    return res if not formato else formatacao(res)

def diminuir(n=0, taxa=0, formato=False):
    res = n - ((taxa / 100) * n)
    return res if not formato else formatacao(res)


def formatacao(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

