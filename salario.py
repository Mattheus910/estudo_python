salario = float(input('Qual é o salário do seu funcionário? R$'))
porcentagem = int(input('Qual a porcentagem de aumento ele receberá ? '))
aumento = salario + (salario * porcentagem / 100)
print(f'Um funcionário que ganhava R${salario}, com {porcentagem}% de aumento, passa a receber R${round(aumento, 2)}')
