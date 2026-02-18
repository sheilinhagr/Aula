# enumerate - enumera iteráveis (índices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista)
#print(next(lista_enumerada))

#lista_enumerada = list(enumerate(lista, start=2))
#print(lista_enumerada)

for item in enumerate(lista):
    #a, b = item
    indice, nome = item
    print(indice, nome)

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# for item in enumerate(lista):
#     print(item)


#for item in lista_enumerada:
    #print(item)