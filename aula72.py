# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador (*args):
    x=1
    for numero in args:
        x*=numero
    print(x)
    return x

multiplicador(1,2,3,4,5,6,7)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def epar (num):
    x=""
    if num%2 == 0:
        x="par"
    else:
         x="impar"
    print(x)
    return x        

epar(25)