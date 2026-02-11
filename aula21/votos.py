def voto(n):
    from datetime import date 
    ano_atual = date.today().year
    idade = ano_atual - n
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')

    elif 16 <= idade < 18 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
        
    elif idade >= 18:
        return print(f'Com {idade} anos: VOTO OBRIGATORIO.')
        

ano = int(input('Em que ano Você nasceu? '))
voto(ano)