#conteúdo = matriz

matriz = [
  [1 ,2, 3]
  [4, 5, 6]
  [7, 8, 9]
]

for l in range(3):
  for c in range(3):
    print(matriz[l][c])


#exemplo 2;

for linha in matriz:
  for num in linha:
     print(num)


#l como linha
#Como coluna 

#desafio:

matriz_d = [
 [1,4,5,9,7,9,7,8,9]
 [1,1,1,3,4,5,9,7,8]
 [1,1,1,1,11,1,1,1,]
]

#removendo em 1 vetor:
x = [1, 2, 3, 4, 8, 9, 9, 9, 9, 7, 7, 8, 1]
y = []
#y recebe uma lista vazia

for z in num:
  if z not in y:
    y.append(z)
x = z
#x ta recebendo o valor de z já tratado, lembrando que x era a variável inicial da lista com n° repetidos,
print(x)          