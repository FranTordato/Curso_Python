velocidade_carro = 60
local_carro = 101
RADAR_1 = 60
LOCAL_1 = 100 #velocidade máxima do radar
RADAR_RANGE = 1 #local onde o radar está;
velocidade_carro_passou = velocidade_carro > RADAR_1
km_99 = LOCAL_1 - RADAR_RANGE
km_101 = LOCAL_1 + RADAR_RANGE
antes_dentro_radar = local_carro >= km_99
depois_dentro_radar = local_carro<=km_101
carro_no_radar = antes_dentro_radar and depois_dentro_radar
carro_multado = carro_no_radar and \
    velocidade_carro_passou 

if velocidade_carro_passou:
        print('vc  passou da velocidade permitida')

if carro_no_radar:
        print('carro passou radar')

if  carro_multado:
        print('o carro foi multado')
        

