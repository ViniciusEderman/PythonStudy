#organizador de código,


def about(alt, name):
  print('=' * 20)
  print('Vinicius Ederman', name)
  print('data = 20/12', alt)
  print('=' * 20)


print('teste inicío')
about()
print('teste fim')


#alterando o about
about('data = 25/12/2021', 'Vinicius Junior')
##
about('data = 01/01/2022', 'Carlos Jose')

def cubo(num):
  return num ** 3 
num = cubo(2)

#2 está retornando no ^ 3,,,
##

def maior(num1, num2):
 if num1 > num2:
   return num1
 else:
   return num2


print(maior(4,9))