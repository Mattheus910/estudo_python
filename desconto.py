preco = float(input('Qual o preço do produto ? R$'))
d = int(input('Qual é o desconto ? '))
novo = preco - (preco * d / 100)
print(f'O produto que custava R${preco}, na promoção com desconto de {d}% vai custar RS{novo:.2f}')
