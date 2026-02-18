# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'


# p,b,*_, ap, u = lista
# print(p,u)

# for nome in lista:
#     #print(nome)
#     print(nome, end=' ')
#print(*lista) #é igual print('Maria', 'Helena', 1, 2, 3, 'Eduarda')

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

#print(salas)
#print(*salas)
#print(*salas, end='\n')
print(*salas, sep='\n') #quebra de linha
