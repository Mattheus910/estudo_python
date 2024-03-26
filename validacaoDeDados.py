s = str(input('Informe seu sexo: [M/F] ')).strip()

while s not in ('FfMm'):
     s = str(input('Dados invalidos. Por favor, informe seu sexo: '))
print(f'Sexo {s.upper()} registrado com sucesso!')


