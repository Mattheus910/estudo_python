from datetime import date

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))


if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - date.today().year)

print('-=' * 20)
for k, v in pessoa.items():
    print(f' - {k.title()} tem o valor {v}')
