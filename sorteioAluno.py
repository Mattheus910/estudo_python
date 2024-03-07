
from random import choice

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print(f'O(a) aluno(a) escolhido(a) foi {choice(lista)}')



'''
import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]


print(f'Aluno(a) escolhido(a) foi {lista[random.randint(0, len(lista) - 1)]}')
'''