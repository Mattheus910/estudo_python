from math import hypot

op = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(op, adj):.2f}')