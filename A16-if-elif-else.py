# if / elif .... / else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair')

print('fora dos blocos if elif else')


#o elif depende do if e do else para existir, já o else pode
#existir somente com o if antes. o if pode existir sozinho