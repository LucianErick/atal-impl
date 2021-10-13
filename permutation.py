# import math

# def solucao(qtd):
#     saida = []
#     for i in range(qtd_entradas):
#         qtd_numeros = input()
#         lista = list(map(int, lista_2.split(" ")))

# def div_e_consquista(lista):
#     resultado = []
#     raiz = max(lista)
#     posicao_raiz = lista.index(raiz)
#     sub_esquerda = sorted(lista[0:posicao_raiz], key=int, reverse=True)
#     sub_direita = sorted(lista[posicao_raiz+1:len(lista)], key=int, reverse=True)
#     for i in range(len(sub_esquerda)):
#         lista.append((sub_esquerda[i], calcula_profundidade(i)))
#     lista.append((raiz, 0))
#     for i in range(len(sub_direita)):
#         lista.append((sub_direita[i], calcula_profundidade(i)))    
#     print (lista)

# def calcula_profundidade(posicao):
#     if (posicao % 1 > 0.5):
#         return 1 + math.ceil(math.sqrt(posicao))
#     else:
#         return 1 + math.floor(math.sqrt(posicao))

# print(div_e_consquista([3,5,2,1,4]))