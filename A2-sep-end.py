# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

#sep é um argumento que funciona como separador para formatação 
# \r\n -> CRLF é padrão de quebra de linha
#colocar end='#' você muda esse padrão com o argumento dentro das ''
# \n -> LF sistema unix

#se eu selecionar print e apertar ctrl + c e na linha abaixo apertar ctrl + v 
# a primeira linha será copiada por inteiro

texto = '\nHoje eu fui na escola\nSegunda linha'
print(texto)

print("Primeira linha", end="")#evita quebra automática
print("continua na mesma linha")
print('Olá\rEl') 
#O \r fez o cursor voltar para o início da linha, 
# e o "El" sobrescreveu os dois primeiros caracteres de Olá