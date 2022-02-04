
#problema baseado na senha#

senha = input('Qual a senha desejada para cadastro?')

if len(senha) >= 10 and len(senha) <= 15:
    print("senha cadastrada!")
else:
    print("Senha não cadastrada")

#senha string

senha_inteira = int(input('Qual a senha desejada para cadastro?'))

if int(len(senha_inteira)) >= 10 and int(len(senha_inteira)) <= 15:
    print("senha cadastrada!")
else:
    print("Senha não cadastrada")
    
#lean != int#
#buscar função que rode numero("no local do lean") 

while True:
  senha = input('Digite sua senha: ')
  list(senha)
  if len(senha) < 6:
    print('Deve conter no mínimo 6 caracteres.')
  elif len(senha) > 10:
    print('Deve conter no máximo 10 caracteres.')
  else:
    if not any(x.isupper() for x in senha):
     print('Deve conter pelo menos uma letra maiúscula.')
    elif any(x.islower() for x in senha):
      print('Deve conter pelo menos uma letra maiúscula.')
    elif any(x.isdigit() == False for x in senha):
      print('Deve conter pelo menos um número.')
    else:
      break
print('Senha válida.')


import re 
password = "R@m@_f0rtu9e$"
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
  
if flag ==-1: 
    print("Not a Valid Password") 