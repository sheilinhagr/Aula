"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter('Sheila') # é a mesma coisa de 'Sheila'.__iter__()


# print(texto.__next__()) # é a mesma coisa que print(next(texto))
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

texto = 'Sheila' # iterável
# iteratador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


