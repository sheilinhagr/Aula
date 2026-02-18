"""
Interpolação básica de strings
s - string
d e i - int
f - float
x(gera um hexad. minúsculo) e X(gera um hexad. maiuscúlo) - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
print('O hexadecimal de %d é %X' % (15, 15))