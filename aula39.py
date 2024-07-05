"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nova_string = ''
contador=0

while contador<len(nome):
    nova_string+= nome[contador]+"*"
    contador+=1


print(nome)
print(nova_string)