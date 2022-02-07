import random
from time import sleep

quantidade = int(input('quantos jogos você quer sortear?: '))
numeros = list()
#contador = 1
print('gerando...')
print()
sleep(0.7)

for contador in range(1, quantidade+1):
  numeros.clear()
  numero = 0
  while numero <6:
   num = random.randint(1,60)
   if num not in numeros:  
    numeros.append(num)
  else:
   continue
numero+=1  
numeros.sort()
sleep(0.3)
print(f'jogo {contador}: {numeros}')
print()
contador+=1
  