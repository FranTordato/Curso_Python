nome = 'fran'
preco = 134.456 

# %s interpolaçaõ de string
#%f interpolação de float('3' quantidade de casas)
 
resultado= '%s ,o preço é %.3f' %(nome,preco)
print(resultado)

#d=int , s=string , f=float , x ou X = hexadecimal
# exemplo de interpolação de valores em hexadecimal
# %d  mostra o primeiro valor informado
# %x mostra o valor hexadecimal do valor informado('04' é a quantidade de casas)

print('O hexadecimal de %d é %04x'% (1234 , 1234))