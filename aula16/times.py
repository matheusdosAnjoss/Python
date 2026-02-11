classificacao = (
    'Palmeiras','Flamengo','Cruzeiro','Mirassol',   'Botafogo', 'Bahia', 'Fluminense', 'São Paulo',     'Vasco', 'Red Bull Bragantino', 'Corinthians',  'Grêmio', 'Ceará', 'Internacional', 'Atlético-MG',  'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport'         
)

print('='*67)
print('Lista de times do Brasileirão: ', end=' ')
print(classificacao)
print('='*67)

print('Os 5 primeiros colocados: ', end=' ')
print(classificacao[0:5])
print('==='*23)

print('Os 4 ultimos são: ', end=' ')
print(classificacao[16:20])
print('==='*23)

print('Times em ordem alfabetica: ', end=' ')
print(sorted(classificacao))
print('==='*23)

print(f'O Corithians está na {classificacao.index('Corinthians')+1} Posição')