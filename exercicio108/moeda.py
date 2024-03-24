def metade(n=0):
    res = n - (n / 2)
    return res

def dobro(n=0):
    res = n * 2
    return res

def aumento(n=0, taxa=0):
    res = n + ((taxa / 100) * n)
    return res

def diminuir(n=0, taxa=0):
    res = n - ((taxa / 100) * n)
    return res


def formatacao(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

