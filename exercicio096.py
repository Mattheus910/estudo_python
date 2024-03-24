def area(l, m):
    a = l * m
    print(f'Á area de um terreno é de {l}x{m} é de {a}m²')

print('Controle de Terrenos')
print('-' * 20)

l = float(input('Largura (m): '))
m = float(input('Comprimento (m): '))

area(l, m)
