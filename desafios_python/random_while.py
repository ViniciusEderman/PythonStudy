import random

num_aleatorio = random.randint(1, 6)

num_de_tentativas = 0

print(num_aleatorio) 
#transformar em comentário na hora de rodar ^^ ##

while num_de_tentativas < 3:
  num_de_tentativas += 1
  num_utilizador = int(input("Tente adivinhar o número aleatório do 01 até 06: ")) 
  if num_utilizador == num_aleatorio:
    print("parabéns você acertou!")
    break
else:
    print("Boa sorte na próxima tentativa:")