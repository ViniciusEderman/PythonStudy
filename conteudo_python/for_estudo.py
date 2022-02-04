 # print com range

num = [1 ,10, 20, 30, 40, 50] 
for num in range(4): 
  print(num)

num = [1, 2, 3, 4, 5, 6]
for num in range(0, 3):
 print(num)

  #exemplos com o uso do range no for

#desafio

num_des = [1, 3, 19, 15, 88, 66, 88]

maior = num_des[0]
for num in num_des:
 if num_des > maior:
    maior = num_des
print(maior)