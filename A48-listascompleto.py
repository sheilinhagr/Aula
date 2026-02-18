"""
listas
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métedos úteis: append, insert, por, del, clear, extend, +
create read update delete = lista[i] (CRUD)
"""
#.........54321
#........-54321
# string = 'ABCDE' # 5 caracteres (len)
# lista = [123, True, 'Sheila', 1.2,[]]
# #print(lista[2].upper(), type(lista[2])) 
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2])) 
# #print(bool(lista)) #Falsy
# #print(lista, type(lista))

#lista = [1,2,3,4]
#numero = lista[2]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50) #adiciona o valor ao final da lista
# lista.pop() #remove o último item da lista ---> 50
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido', ultimo_valor)

# lista = [10, 20, 30, 40]
# lista.append('She')
# nome = lista.pop()
# lista.append(2222)
# del lista[-1] #remove o último item da lista
# #lista.clear() limpa a lista
# lista.insert(0, 5) # 0 é o indice a ser inserido e o 5 é o valor a ser inserido.
# print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)