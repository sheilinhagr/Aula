"""
split e join com list e str
split divide uma string
join  une uma string

"""
frase = '  Olha só que  ,    coisa interessante'
lista_palavras = frase.split(', ')

lista_palavras_fixed = []
for i, frase in enumerate(lista_palavras):
    #print(lista_palavras[i])
    #print(lista_palavras[i].lstrip())
    #print(lista_palavras[i].strip())
    #strip corta os espaços
    #lista_palavras[i] = lista_palavras[i].strip()
    lista_palavras_fixed.append(lista_palavras[i].strip())


# print(lista_palavras)
# print(lista_palavras_fixed)

#frases_unidas = '-'.join('abc')
frases_unidas = '-'.join(lista_palavras_fixed)
print(frases_unidas)