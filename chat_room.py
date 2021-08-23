palavra = "hello"
 
def solucao():
  contador = 0
  texto = input()
  for i in range(len(texto)):
    if texto[i] == palavra[contador]:
      contador += 1
    if contador == 5:
      return "YES"
  return "NO"

print(solucao())