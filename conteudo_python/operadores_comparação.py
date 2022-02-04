# < menor 
# < maior 
# <= menor ou igual
# >= maior ou igual
# == igual
# != diferente 

#exercício básico

senha = input("Introduza a senha entre 6 ou 15 caracteres: ")
if len(senha) >= 6 and len(senha) <=15:
    print("Sua senha está válida")
else:
    print("sua senha não é válida")

    #len é para contagem de caracteres 

    