# frase = 'O python é uma linguagem de programação '\
#     'multiparadigma. '\
#     'python foi criado por Guido van Rossum.'#.lower()
frase = 'aaaooo'

#print(frase.count('o'))

i = 0
qtd_apareceu_mais_vzs = 0
letra_apareceu_mais_vzs = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    
    qtd_apareceu_mais_vzs_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vzs < qtd_apareceu_mais_vzs_atual:
        qtd_apareceu_mais_vzs = qtd_apareceu_mais_vzs_atual
        letra_apareceu_mais_vzs = letra_atual

    #print(letra_atual, qtas_vzs_letra_apareceu)
    i += 1

print(f'A letra que apareceu mais vezes foi"{letra_apareceu_mais_vzs}" e {qtd_apareceu_mais_vzs}x')
