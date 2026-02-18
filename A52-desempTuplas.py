#Exemplo 1:
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes # é igual: nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# exemplo 2:
# nome1, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome1, resto)

#exemplo 3:
# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome1, _)

#exemplo 4:

# _, nome2, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome2)

#exemplo 5:

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)