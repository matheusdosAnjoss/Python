teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Matheus'
teste[1] = 21
galera.append(teste[:])
print(galera)