import os
lista=[]


while True:
    print(f'Selecione uma opção')
    opcao=input("[i]nserir ; [a]pagar ; [l]istar ")

    if opcao == 'i':
        os.system('cls')
        lista.append(input('digite o valor: '))
    elif opcao == 'a': 
        os.system('cls')   
        indice_str=input("Digite um indice: ")

        try:
            indice=int(indice_str)
            try:
                del lista[indice]
            except IndexError:
                print('Digite um indice Valido')
        except ValueError:
            print('Por Favor Digite apenas números inteiros.')

    elif opcao == 'l':
        os.system('cls')

        if len(lista)>0:
            print('Itens da lista:')
            for i, nome in enumerate(lista):
                print(f"\t{i}, {nome}")
        else:
            print('LISTA VAZIA')

    else:
        os.system('cls')
        print('Opção Invalida ')