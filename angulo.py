from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo que você deseja: '))
radiano = radians(angulo)

print(f'O ângulo de {angulo} tem o SENO de {sin(radiano):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radiano):.2f}')
print(f'O ângulo de {angulo} tem o TANGENTE de {tan(radiano):.2f}')
