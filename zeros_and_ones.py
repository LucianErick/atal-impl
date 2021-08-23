qtd_digitos = int(input())
digitos = list(map(int, input().replace('', ' ').strip().split(' ')))

qtd_zeros = digitos.count(0)
qtd_uns = digitos.count(1)

print (abs(qtd_zeros - qtd_uns))