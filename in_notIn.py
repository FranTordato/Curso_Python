#em python strings são iteraveis(navegar item por item)
#F R A N 
#-4 -3 -2 -1
#0 1 2 3 

#nome='Fran'
#print('F'in nome)
#print('o' in nome)
#print(10*'-')
#print('F'not in nome)
#print('o'not in nome)

nome = input('digite seu nome: ')
busca = input('digite sua busca: ')

if busca in nome :
    print (f'{busca} está em {nome}')

else:
    print(f'{busca} não está em {nome}')
