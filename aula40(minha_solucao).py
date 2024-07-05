while True:
    valor1=None
    valor2=None
    operador=None
    while True:
        print('qual operação você deseja realizar?')
        operador=input('[A]dição, [S]ubtração, [M]ultiplicação, [D]ivisão: ').upper()
        print(operador)
        if operador.startswith('A') or operador.startswith('S') \
        or operador.startswith('M') or operador.startswith('D'):
            break
        else:
            print('Opção invalida digite uma opçãp valida')
            continue
            
        pause
    while True:
        try:
            valor1=float(input("Digite um numero: "))
            valor2=float(input("Digite outro numero: "))
        except:
            print('Um ou ambos os números digitados são inválidos')
            continue
        break
    
    print(operador)
    print(valor1)   
    print(valor2)   


    if operador == "A":
        print(f"A soma de {valor1} + {valor2} = {valor1+valor2}")
    if operador == "S":
        print(f"A soma de {valor1} - {valor2} = {valor1-valor2}")
    if operador == "M":
        print(f"A soma de {valor1} X {valor2} = {valor1*valor2}")
    if operador == "D":
        print(f"A soma de {valor1} / {valor2} = {valor1/valor2}")

    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    
    if sair:
        break


