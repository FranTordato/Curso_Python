#or se 1 é verdadeiro ,todos são verddeiros

entrada= input('Digite E para entrar e S para sair: ')
senhaDigitada =input('Digite sua senha: ')
senhaCorreta = '1234'

if (entrada == 'E' or entrada == 'e')and senhaDigitada == senhaCorreta:
    print ('Você entrou no sistema')

else:
    print('Você saiu do sistema')

#AVALIAÇÃO DE CURTO CIRCUITO
senha = input('senha : ')or ('sem senha')
print(senha)
    
numero = 10
     
