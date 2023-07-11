"""
Flag(bandeira)-marca um local
None =não valor
is ou is not= é ou não é(valor,tipo,identidade)
id=Identidade

"""
condicao=False
passou_no_if=None

if condicao:
     passou_no_if=True
     print ('Faça algo')

else:
     print('não faça algo')

if passou_no_if is None:
     print('não passou no if')

if passou_no_if is not None:
     print('Passou no if')