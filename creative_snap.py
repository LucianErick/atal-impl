def custo_minimo(l, r, lista):
    
    if(len(lista) == 0):
        return a

    elif(l == r):
        return b * len(lista)

    else:
        meio = (l + r) // 2
        tras = []
        frente = []
        for elemento in lista:
            if(elemento <= meio):
                tras.append(elemento)
            else:
                frente.append(elemento)
        
        return min(b * len(lista) * (r - l + 1), custo_minimo(l, meio, tras) + custo_minimo(meio + 1, r, frente))
 
def potencia(base, expoente):
    return base ** expoente

n, k, a, b = map(int, input().split(" "))
lista = list(map(int,input().split(" ")))

lista.sort()

print(custo_minimo(1, potencia(2, n), lista))