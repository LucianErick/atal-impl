def resolucao():
    contador = 0
    for i in range(qtdTimes):
        for j in range(qtdTimes):
            if (i == j):
                continue
            if (equipes[i][0] == equipes[j][1]):
                contador += 1
    return contador


def le_entradas(qtd):
    for equipe in range(qtd):
        uniformes = ()
        input_uniformes = input().split(" ")
        equipes.append((int(input_uniformes[0]), int(input_uniformes[1])))

qtdTimes = int(input())
equipes = []
le_entradas(qtdTimes)
print(resolucao())
