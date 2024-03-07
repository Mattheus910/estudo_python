numero = int(input("Digite um numero para ver a tabuada: "))

print("------------")

for n in range(1, 11):
    print(f'{numero} x {n:2} = {numero * n}')

print("------------")
