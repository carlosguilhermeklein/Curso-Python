import random
cpf= ""
for i in range(9):
    cpf+=str(random.randint(0,9))


# remove pontos e ifens
cpf_calc=""

for i in cpf:
    if i.isdigit():
        cpf_calc+=i
nove_digitos=cpf_calc
primeiro=0
verificador=10
for numero in cpf:
    if numero.isdigit() and verificador>=2:
        primeiro+=(int(numero)*verificador)
        verificador-=1
primeiro*=10
primeiro = primeiro%11
if primeiro>9:
    primeiro=0

print(primeiro)

# ajusta cpf para 9 digit + o primiro
cpf_calc=cpf_calc[0:9]+str(primeiro)

segundo=0
multiplicador=11
for i in cpf_calc:
    segundo+=(int(i)*multiplicador)
    multiplicador-=1

segundo=segundo*10
segundo=segundo%11
if segundo>9:
    segundo=0
print(segundo)
cpf= cpf+str(primeiro)+str(segundo)

cpf_montado=""
contador=0
for i in cpf:
    if contador == 2:
        cpf_montado+=str(i)+"."
    elif contador == 5:
        cpf_montado+=str(i)+"."
    elif contador == 8:
        cpf_montado+=str(i)+"-"
    else:
        cpf_montado+=str(i)
    contador+=1    

print(cpf_montado)









