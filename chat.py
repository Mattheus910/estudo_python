import os

mensagens = []

nome = input("Nome: ")

while True:

    # Limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_______________")

    #obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem a lista

    mensagens.append(
        {
            "nome": nome,
            "texto": texto,
        }
    )

