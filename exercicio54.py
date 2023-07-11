

entrada= input ('Digite um numero inteiro: ')

if entrada.isdigit():
     numero= float(entrada)
     par=numero % 2 == 0
     
     if  par is True:
      print(f'O número {entrada} é par')
     elif par is False:
       print(f'O número {entrada} é impar')
    
     
else:   
       print('você não digitou um número inteiro')
      



hora = int (input ('Digite a hora: '))

if hora<=11:
        print('Bom dia')
elif hora>=11 and hora <= 17 :
        print('Boa tarde')
elif hora>=18 and hora <= 23 :
        print('Boa noite')

primeiro_nome=input('Digite seu primeiro nome: ')
primeiro_nome=len(primeiro_nome)

if primeiro_nome <=4:
     print('seu nome é curto')
elif primeiro_nome>=5 and primeiro_nome<=6:
     print("Seu nome é normal")
elif primeiro_nome >=7:
     print("Seu nome é muito grande")


