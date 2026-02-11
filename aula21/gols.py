def placar(time1, gol1, time2, gol2):
    print('=='*15)
    print(f'{time1} {gol1} x {gol2} {time2}')
    print('=='*15)

    if gol1 > gol2:
        return print(f'{time1} Venceu a partida!')
    elif gol2 > gol1:
        return print(f'{time2} Venceu a partda! com {gol2} gols')
    elif gol1 == gol2:
        return print('A partida terminou empatada!')

placar('flamengo', 5, 'palmeiras', 3)