
nome = str(input('Digite seu nome completo: '))
letras = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len("".join(letras))} letras')
print(f'Seu primeiro nome é {letras[0]} e ele tem {len(letras[0])} letras')
