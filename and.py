#em python os valores 0 , 0.0 , e '' sao considerados falsy(falso)
#and se 1 é false todos são falsos

entrada = input ('[E]ntrar [S]air: ')

senha_digitada=input('digite a senha: ')
senha_correta='1234'
if entrada == 'E' and senha_digitada == senha_correta:
    print('você entrou no sistema')

else :
    print ('você saiu do sistema')

#avaliação de curto circuito
#print(true and true and false)