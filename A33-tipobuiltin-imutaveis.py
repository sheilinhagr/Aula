"""
https://docs.python.org/pt-br/3/library/stdtypes.html
imutáveis que vimos: str, int, float, bool

"""
string = 'Sheila Gomes'
outra_variavel = f'{string[:3]}rezende'
outra_variavel = f'{string[:3]}rezende{string[4:]}'

#print(string[4])
print(outra_variavel)
print(string.upper())
print(string.zfill(33))
print(string.center(10))