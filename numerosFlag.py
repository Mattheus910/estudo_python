
n = 0
c = 0
s = 0

while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}')



