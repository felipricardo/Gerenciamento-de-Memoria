import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
memoria = [' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ']
#for i in range(100):
#    if(random.randint(0,11) >= 5):
#        memoria[i] = 'x'
#    else:
#        memoria[i] = ' '
#print(memoria)

#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):
    print(memoria[i],end="|")
print()
for i in range(20,40):
    print(memoria[i],end="|")
print()
for i in range(40,60):
    print(memoria[i],end="|")
print()
for i in range(60,80):
    print(memoria[i],end="|")
print()
for i in range(80,100):
    print(memoria[i],end="|")
print()
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utilizada")
    letra = input()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        ini = 0
        while ini < 100:

            if memoria[ini] == ' ':
                print("Inicio", ini)
                fim = ini + 1
                while fim < 100:
                    if memoria[fim] != ' ':
                        break
                    fim += 1
                print("fim", fim)
                tamanhodoburaco = fim - ini
                print("Tamanho buraco", tamanhodoburaco)
                if tamanhodoburaco >= tamanho:
                    print("Grande o suficiente")
                ini = fim + 1
        pass
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            pass
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                pass
    # Aqui você deve imprimir todo o conteúdo da variável memória
    for i in range(0,20):
        print(memoria[i],end="|")
    print()
    for i in range(20,40):
        print(memoria[i],end="|")
    print()
    for i in range(40,60):
        print(memoria[i],end="|")
    print()
    for i in range(60,80):
        print(memoria[i],end="|")
    print()
    for i in range(80,100):
        print(memoria[i],end="|")
    print()
