from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
sair = False
while sair != True:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} + {valor2} é {soma}')
        print('-==' * 10)
    elif opcao == 2:
        mult = valor1 * valor2
        print(f'O resultado de {valor1} x {valor2} é {mult}')
        print('-==' * 10)
    elif opcao == 3:
        aux = 0
        if valor2 > valor1:
            aux = valor1
            valor1 = valor2
            valor2 = aux
        print(f'Entre {valor1} e {valor2} o maior é {valor1}')
        print('-==' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        print('-==' * 10)
    elif opcao == 5:
        sair = True
        print('-==' * 10)
    else:
        print('Opção inválida. Tente novamente')


print('Finalizando...')
sleep(1)
print('Fim do programa! Volte Sempre!')
