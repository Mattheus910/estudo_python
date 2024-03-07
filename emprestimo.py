casa = int(input('Valor da casa? '))
salario = float(input('Salario do comprador? '))
anos = int(input('Quantos anos de financiamento? '))

porcentagem = salario * 30 / 100
mensal = (casa / anos) / 12

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${mensal:.2f}')

if mensal < porcentagem:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

