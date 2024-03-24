matriz = [[], [], []], [[], [], []], [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para a matriz [{l}, {c}]: '))
        matriz[l][c].append(n)

print("-=" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}:^5]', end='')
        print()
