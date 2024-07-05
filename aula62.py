"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""



cpf= "019.775.770-75"
# remove pontos e ifens
cpf_calc=""
for i in cpf:
    if i.isdigit():
        cpf_calc+=i


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







