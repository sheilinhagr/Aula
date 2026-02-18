a = 'A'
b = 'B'
c = 1.1
#exemplo 1:

# formato = 'a={} b='.format(a, b, c)

#exemplo2:
# string = 'a={} b={} c={}'
# formato = string.format(a, b, c)

#Exemplo 3:

# string = 'a={} b={} c={:.2f}'
# formato = string.format(a , b , c)

#Exemplo 4:
# string = 'a={0} b={1} c={2:.2f}' #assim foi colocado os indices
# #string = 'a={1} b={1} c={2:.2f}'
# formato = string.format(a , b , c)

# Exemplo 5:

string = 'a={nome1} a={nome1} b={nome2} b={nome2} c={nome3:.2f}'
#string = 'a={1} b={1} c={2:.2f}'

formato = string.format(
    nome1=a, nome2=b, nome3=c) 
#tudo que vem depois de um parâmetro nomeado precisa ser nomeado -->nome3=c

print(formato)

#A função format() em Python é um método de string para formatar texto, 
# substituindo espaços reservados {} 
# por valores de variáveis de forma organizada
#Usando espaços reservados: Insira chaves {} 
# na string onde você quer que os valores sejam inseridos
