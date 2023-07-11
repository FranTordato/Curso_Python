#formatação 4 tipos

#primeiro
a=1.0
b=2.0
c=3.0
frase_1 = f'a ={a} b= {b} c= {c:.2f}'
print(frase_1)

#segundo

a=1.0
b=2.0
c=3.0
letras = 'a={} b={} c={:.2f}'
frase_2 = letras.format (a , b, c)
print(frase_2)

#terceiro...utilizando indices

a=1.0
b=2.0
c=3.0
letras = 'a={0} b={1} c={2:.2f}'
frase_3 = letras.format (a , b, c)
print(frase_3)

#quarto..nomeando

a=1.0
b=2.0
c=3.0
letras = 'a={nome_1} b={nome_2} c={nome_3:.2f}'
frase_3 = letras.format (nome_1=a , nome_2=b, nome_3=c)
print(frase_3)


