from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue adivinhar qual foi?')

palpite = int(input('Qual é seu palpite? '))
computador = randint(0, 10)
tentativas = 1


while palpite != computador:
    if computador > palpite:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativas += 1
    else:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
