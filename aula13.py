nome = 'Carlos Klein'
altura = 1.80
peso = 110
imc=peso/(altura*altura)

print(nome +" tem "+str(altura)+" de altura,")
print("pesa "+str(peso)+" quilos e seu IMC é")
print(imc)

linha1= f"{nome}  tem {altura:.2f} de altura,"
linha2= f"pesa {peso} quilos e seu IMC é"
linha3= f"{imc:.2f}"
print(" ")
print(linha1)
print(linha2)
print(linha3)