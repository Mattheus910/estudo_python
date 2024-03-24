jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partidas = list()
for c in range(tot):
    partidas.append(int(input(f' Quantos gols na partida {c}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for k, v in enumerate(partidas):
    print(f' => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
