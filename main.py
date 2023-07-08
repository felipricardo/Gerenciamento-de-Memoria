import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''

for i in range(100):
    if random.randint(0, 11) >= 5:
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

# print estágio inicial da memória

tamanholinha = 20
proxlinhalivre = 20

for i in range(100):
    if i < (tamanholinha - 1):
        print(memoria[i], end='|')
    else:
        print(memoria[i], end='\n')
        tamanholinha += proxlinhalivre

# menu
opcao = 0
while (opcao != 4):
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo número")
    opcao = int(input())

    print("Digite o tamanho da informação")
    tamanho = int(input())
    print("Digite a letra a ser gravada")
    letra = input()

    # primeira opção
    if opcao == 1:
        print('1 - Primeira Escolha')
        espaco_encontrado = False
        for i in range(100):
            if memoria[i] == ' ':
                contadorproxvazio = 1
                while contadorproxvazio < tamanho:
                    if memoria[i + contadorproxvazio] != ' ':
                        break
                    contadorproxvazio += 1
                if contadorproxvazio == tamanho:
                    espaco_encontrado = True
                    indexinicio = i
                    indexfinal = i + tamanho - 1
                    for j in range(indexinicio, indexfinal + 1):
                        memoria[j] = letra
                    break

        if espaco_encontrado:
            # print novo estágio da memória
            proxlinhalivre = 20
            tamanholinha = 20
            for i in range(100):
                if i < (proxlinhalivre - 1):
                    print(memoria[i], end='|')
                else:
                    if i == (proxlinhalivre - 1):
                        print(memoria[i], end='\n')
                        proxlinhalivre += tamanholinha
        else:
            print('Informação excede espaço disponível')

    # segunda opção
    elif opcao == 2:
        print('2 - Melhor Escolha')
        espaco_encontrado = False
        melhorescolha = float('inf')
        indexmelhorescolha = 0
        espaco_atual = 0

        for i in range(100):
            if memoria[i] == ' ':
                espaco_atual += 1
                if espaco_atual >= tamanho:
                    espaco_encontrado = True
                    if espaco_atual - tamanho < melhorescolha:
                        melhorescolha = espaco_atual - tamanho
                        indexmelhorescolha = i - espaco_atual + 1
            else:
                espaco_atual = 0

        if espaco_encontrado:
            indexinicio = indexmelhorescolha
            indexfinal = indexmelhorescolha + tamanho - 1
            for j in range(indexinicio, indexfinal + 1):
                memoria[j] = letra

            # print novo estágio da memória
            proxlinhalivre = 20
            tamanholinha = 20
            for i in range(100):
                if i < (proxlinhalivre - 1):
                    print(memoria[i], end='|')
                else:
                    if i == (proxlinhalivre - 1):
                        print(memoria[i], end='\n')
                        proxlinhalivre += tamanholinha
        else:
            print('Informação excede espaço disponível')

    # terceira opção
    elif opcao == 3:
        print('3 - Pior Escolha')
        espaco_encontrado = False
        piorescolha = -1
        indexpiorescolha = 0
        for i in range(100):
            if memoria[i] == ' ':
                contadorproxvazio = 1
                while contadorproxvazio < tamanho:
                    if memoria[i + contadorproxvazio] != ' ':
                        break
                    contadorproxvazio += 1
                if contadorproxvazio == tamanho:
                    espaco_encontrado = True
                    espaco_disponivel = contadorproxvazio - tamanho
                    if espaco_disponivel > piorescolha:
                        piorescolha = espaco_disponivel
                        indexpiorescolha = i
        if espaco_encontrado:
            indexinicio = indexpiorescolha
            indexfinal = indexpiorescolha + tamanho - 1
            for j in range(indexinicio, indexfinal + 1):
                memoria[j] = letra

            # print novo estágio da memória
            proxlinhalivre = 20
            tamanholinha = 20
            for i in range(100):
                if i < (proxlinhalivre - 1):
                    print(memoria[i], end='|')
                else:
                    if i == (proxlinhalivre - 1):
                        print(memoria[i], end='\n')
                        proxlinhalivre += tamanholinha
        else:
            print('Informação excede espaço disponível')

    elif opcao == 4:
        break

    else:
        print('Opção inválida. Tente novamente.')
#Felipe Barbosa Mourão
