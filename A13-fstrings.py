nome = 'Sheila'
altura = 1.60
peso = 62
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura' #2f 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)