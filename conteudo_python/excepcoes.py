#exemplo 1,

try:
  idade = int(input("Idade: "))
  print(idade)
except ValueError:
  print("Utilizar somento números")
print('Fim do programa')

#caso eu use string, o programa não irá rodar, sendo o print apenas para números inteiros

#exemplos 2,

try:
  idade = int(input('Idade: '))
  print(idade)
  salario = 1600
  risco = salario / idade
except ValueError:
  print("A idade não é válida, apenas números inteiros são aceitos")
except ZeroDivisionError:
  print("Não pode ser dividido por 0")
print("Fim do programa!")


#dois usos do except,,,