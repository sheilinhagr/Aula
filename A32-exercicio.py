"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um número inteiro: ')

# if entrada.isdigit():
#     num_int = int(entrada)

#     if num_int % 2 == 0:
#         print(f'O número {entrada} é par')
#     else:
#         print('O número digitado é ímpar.')
# else:
#     print('Você não digitou um número inteiro! ')
# try:
#     numero = int(input("Digite um número inteiro: "))
    
#     if numero % 2 == 0:
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} é ímpar.")

# except ValueError:
#     print("Você não digitou um número inteiro.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora_atual = input('Quantas horas? ')

# try:
#     hora = int(hora_atual)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia! ')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde! ')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora.') 

# except:
#     print('Digite somente números inteiros.')

"""
try:
    hora = int(input("Que horas são (0-23)? "))

    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida! Digite um número entre 0 e 23.")

except ValueError:
    print("Você não digitou um número inteiro.")

"""




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual é o seu primeiro nome? ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')

else:
    print('Digite mais de uma letra.') 