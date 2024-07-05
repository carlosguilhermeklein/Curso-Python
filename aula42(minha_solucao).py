frase= 'O Python é uma linguagem de programação' \
        'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum.'
i=0
letra_que_mais_apareceu=None
while i <len(frase):
    letra_atual=frase[i]

    if letra_atual== " ":
        i+=1
        continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)
   
    if letra_que_mais_apareceu == None:
        letra_que_mais_apareceu=letra_atual
    if quantas_vezes_letra_apareceu > frase.count(letra_que_mais_apareceu):
        letra_que_mais_apareceu=letra_atual

    i+=1
print(f"o caractere que mais apareceu é '{letra_que_mais_apareceu}' ele apareceu {frase.count(letra_que_mais_apareceu)} X")