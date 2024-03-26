def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\33[31mERRO! Por favor digite um numero inteiro válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\33[31mUsuario preferiu não digitar esse numero!\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\33[31mERRO! Por favor digite um numero Real válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\33[31mUsuario preferiu não digitar esse numero!\033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'Os valores digitados foram: Inteiro: {n1} e Real: {n2}')