#tabuada

contador1=0
contador2=0

while contador1<=10:
    print(f"Tabuada do {contador1}")
    while contador2<=10:
        print(f"{contador1} X {contador2} = {contador1*contador2}")
        contador2+=1

    contador1+=1
    contador2=0    