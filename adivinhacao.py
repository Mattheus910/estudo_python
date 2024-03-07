from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

numero = int(input('Em que numero eu pensei? '))
random = randint(0, 5)

print('PROCESSANDO...')
sleep(3)

if numero == random:
    print('PÁRABENS! você conseguiu me vencer!')
else:
    print(f'GANHEI! pensei no número {random} e não no {numero}!')
