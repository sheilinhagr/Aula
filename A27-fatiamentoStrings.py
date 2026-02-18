"""
fatiamento de strings
012345678
olá mundo
-987654321
fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd
de caracteres de str
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[:5])
print(variavel[0:5])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:4])
print(variavel[-1:-10:-1])
print(variavel[::-1])