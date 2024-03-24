def voto(ano):
    """
    Função que analisa se o usuario pode votar, se é opcional ou obrigado a votar.
    Args:
        ano: ano de nascimento do usuario.

    Returns: retorna a idade do usuario e sua situação a votação.

    """
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

print('-' * 30)

ano = int(input('Em que ano você nasceu? '))

print(voto(ano))



