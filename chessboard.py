def organiza_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        entrada = input().replace("", " ")
        coluna = entrada.split(" ")
        matriz.append(coluna)
    return matriz
 
def resolucao(matriz):
    retorno = matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = retorno[i][j]
            if (elemento == "."):
                if ((i + j) % 2 == 0):
                    retorno[i][j] = "B"
                else:
                    retorno[i][j] = "W"
    return retorno
 
def imprime_saida(matriz):
    separador = ""
    for i in range(len(matriz)):
        matriz[i] = [separador.join(matriz[i])]
        print(matriz[i][0])
 
tamanho_matriz = input().split(" ")
linhas = int(tamanho_matriz[0])
colunas = int(tamanho_matriz[1])
 
matriz = organiza_matriz(linhas, colunas)
imprime_saida(resolucao(matriz))