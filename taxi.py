qtd_grupos = int(input())
grupos = input().split(" ")
qtd_taxis = 0
 
qtd_taxis += grupos.count('4')
 
grupos_1 = grupos.count('1')
grupos_2 = grupos.count('2')
grupos_3 = grupos.count('3')
 
qtd_taxis +=  grupos_2 // 2
 
grupos_2 = grupos_2 % 2
 
if(grupos_1 <= grupos_3):
    qtd_taxis += grupos_1
    qtd_taxis += grupos_2
    qtd_taxis += grupos_3 - grupos_1
else:
    qtd_taxis += grupos_3
    grupos_1 -= grupos_3
    qtd_taxis += grupos_1 // 4
    grupos_1 = grupos_1 % 4
 
    rest = grupos_1 + grupos_2 * 2
 
    if(rest > 0):
        if(rest <= 4):
            qtd_taxis += 1
        else:
            qtd_taxis += 2
 
print(qtd_taxis)

