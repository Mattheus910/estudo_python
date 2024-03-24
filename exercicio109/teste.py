import moeda


preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.formatacao(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.formatacao(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(preco, 10, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10, True)}')
