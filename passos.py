quantidade_passos = int(input('Digite a quantidade de passos: '))

def verificadorDePassos(passos):
  if passos <= 0:
    print("Nenhum passo dado na floresta.")
  else:
    for passo in range(1, passos + 1):
        if passo == 1:
            print(f'Explorador: {passo} passo')
        else:
            print(f'Explorador: {passo} passos')

verificadorDePassos(quantidade_passos)