#try=tentar
#except=exceção
numero_digitado=input('vou dobrar o numero digitado: ')

try:
    numero_float=float(numero_digitado)
    print(f'o dobro de {numero_digitado} é {numero_float * 2:.2f}')
except:
    print('isso não é um número válido')
    


#if numero_digitado.isdigit():
#    numero_float=float(numero_digitado)
#    print(f'o dobro de {numero_digitado} é {numero_float * 2:.2f}')
#else:
#    print('isso não é um número válido')
    