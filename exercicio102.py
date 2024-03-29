import math
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    Args:
        num: O número a ser calculado.
        show: (opcional) mostra ou não a conta.

    Returns: O valor fatorial de um num

    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fatorial(6, show=True))

help(fatorial)
