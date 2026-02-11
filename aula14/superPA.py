#primeiro = int(input('Primeiro termo: '))
#razao = int(input("Razao da PA: "))

#termo = primeiro
#cont = 1
#total = 0
#mais = 10

#while mais != 0:
#    total += mais
 #   while cont <= total:
#        print(f'{termo} -> ' , end=' ')
 #       termo += razao
 #       cont += 1
#            
 #   print('PAUSA')

#    mais = int(input('Quantos termos você quer mostrae a #mais? '))
#print('FIM')

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

cont = 1
mais = 10
total = 0


while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} -> ', end=' ')
        primeiro += razao
        cont += 1
    
    print('Pausa')

    mais = int(input('Quantos termos você quer a mais ? '))

print(f'Foi somado {total} termos de PA')
