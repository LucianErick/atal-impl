def reduz_numero(lista):
    if (all((digito == 0 or digito == 1) for digito in lista)):
        return lista

    elif (len(lista) == 1):
        primeiro_digito = lista[0] // 2
        segundo_digito = lista[0] % 2
        terceiro_digito = lista[0] // 2
        return reduz_numero([primeiro_digito, segundo_digito, terceiro_digito])
    else:
        resultado = []
        for digito in lista:
            resultado += reduz_numero([digito])
        return reduz_numero(resultado)
        
def codifica_numero(numero):
    if (numero == 0 or numero == 1):
        return numero
    else:
        primeiro_digito = reduz_numero([numero // 2])
        segundo_digito = reduz_numero([numero % 2])
        terceiro_digito = reduz_numero([numero // 2])
        return primeiro_digito + segundo_digito + terceiro_digito

entrada = int(input("Digite um número: "))
saida = codifica_numero(entrada)
print ("O número codificado é: ", saida)
