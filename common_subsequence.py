def resolucao(lista_1, lista_2):
    sub_sequencia = []
    tamanho_subsequencia = 0

    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if(lista_1[i] == lista_2[j] and tamanho_subsequencia == 0):
                sub_sequencia.append(lista_1[i])
                tamanho_subsequencia += 1
    
    if (tamanho_subsequencia == 0):
        print("NO")
    else:
        print("YES")
        print(tamanho_subsequencia, sub_sequencia[0])
    


def le_teste(qtd):
    for i in range(qtd):
        tamanho_listas = input().split(" ")
        
        lista_1 = input()
        lista1_numeros = list(map(int, lista_1.split(" ")))

        lista_2 = input()
        lista2_numeros = list(map(int, lista_2.split(" ")))

        resolucao(lista1_numeros, lista2_numeros)

qtd_testes = int(input())
le_teste(qtd_testes)