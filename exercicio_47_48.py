
nome = (input(f'digite seu nome: '))
idade= (input(f'digite sua idade: '))

if nome  and  idade:
    
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade} anos')
    print(f'Seu nome invertido é: {nome[ : :-1]}')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    print (f'seu nome contem {len(nome)} letras')
    
    if ' ' in nome :
     print ('Seu nome contém espaços')
    else:
       print('Seu nome não contém espaços') 
         
else:
    print('Desculpe ,você deixou campos vazios')

