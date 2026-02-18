"""
Constante - "variáveis" que não vão mudar
muitas condições no mesmo if (ruim)

"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

radar_1 = 60 # velocidade máxima do radar 1
local_1 = 100 # local onde o radar 1 está
radar_range = 1 # a distância onde o radar pega

vel_carro_pass_radar1 = velocidade > radar_1
carro_passou_radar1 = local_carro >= (local_1 - radar_range) and \
    local_carro <= (local_1 + radar_range)
carro_multado_radar_1 = carro_passou_radar1 and vel_carro_pass_radar1

if vel_carro_pass_radar1:
    print('A velocidade do carro passou do radar 1')

if carro_passou_radar1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('carro multado no radar 1')

