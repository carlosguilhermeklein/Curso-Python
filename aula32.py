"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero1=input('Digite um numero inteiro: ')

if numero1.isdigit():

    if int(numero1)%2==0:
        print(f'{numero1} é par')
    else:
       print(f'{numero1} é impar') 

else :
    print('Você não digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora=input('Digite que horas são: ')

if hora.isdigit():
    hora=int(hora)
    if hora >=0 and hora <=11:
        print('Bom Dia')
    elif hora >=12 and hora <=17:
        print('Boa Tarde')
    elif hora >=18 and hora <=23:
        print('Boa Noite')
    else:
        print('Voce não digitou uma Hora valida')

else:
    print("digite apenas a Hora")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome=input('Digite seu primeiro nome: ')
nomelen=len(nome)

if nomelen > 1:
    if nomelen<=4:
        print('Seu nome é curto')
    elif nomelen>=5 and nomelen<=6:
        print('Seu nome é normal')
    elif nomelen>=6:
        print('Seu nome é muito grande')

else:
    print('digite mais de uma letra')