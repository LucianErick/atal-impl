def resolucao(qtdNumeros, listaNumeros):

    qtdImpares = 0
    qtdPares = 0
    indice_diferente_par = 0
    indice_diferente_impar = 0

    for indiceNumero in range(0, qtdNumeros):
        if (listaNumeros[indiceNumero] % 2 == 0):
            indice_diferente_par = indiceNumero
            qtdPares += 1
        else:
            indice_diferente_impar = indiceNumero
            qtdImpares += 1

    if (qtdPares == 1):
        return indice_diferente_par + 1
    return indice_diferente_impar + 1

qtd = int(input())
lista = input()
listaNumeros = list(map(int, lista.split(" ")))

print (resolucao(qtd, listaNumeros))