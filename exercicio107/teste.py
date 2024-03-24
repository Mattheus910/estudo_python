import moeda


numero = float(input('Digite o preço: R$'))

print(f'A metade de R${numero} é R${moeda.metade(numero)}')
print(f'O dobro de R${numero} é R${moeda.dobro(numero)}')
print(f'Aumentando 10%, temos {moeda.aumento(numero, 10)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(numero, 10)}')
