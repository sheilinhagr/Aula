"""
For + Range
range -> range(start, stop, step)
"""
#numeros = range(10) # final até 10
# numeros = range(5, 10)
# numeros = range(5, 10, 2) # step 2
# print(numeros[5]) # mostra o indice 5
numeros = range(10, -1, -1) # contagem regressiva até 0
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
