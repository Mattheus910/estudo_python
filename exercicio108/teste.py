import moeda


preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.formatacao(preco)} é {moeda.formatacao(moeda.metade(preco))}')
print(f'O dobro de {moeda.formatacao(preco)} é {moeda.formatacao(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumento(preco, 10))}')
print(f'Diminuindo 10%, temos {moeda.formatacao(moeda.diminuir(preco, 10))}')
