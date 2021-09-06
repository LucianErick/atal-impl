def solucao(string):
    if len(string) % 2 : 
        return string
    substring_a = solucao(string[:len(string)//2])
    substring_b = solucao(string[len(string)//2:])
    
    if (substring_a < substring_b):
        return substring_a + substring_b
    else:
        return substring_b + substring_a

print('YES' if solucao(input()) == solucao(input()) else 'NO')