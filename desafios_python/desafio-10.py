
try:
    preco = int(input("Introduzir o preço do produto: "))
except ValueError: 
 print('O preço não é válido')

try:
    desconto = int(input("Introduza a porcentagem do desconto: "))
except ValueError:
    print('O desconto não é válido')
     
try:
    valor_pagar = preco - preco * (desconto / 100)
    print("Valor a pagar: ", valor_pagar)  
except NameError:
    print('O programa não consegue calcular o desconto, falta informações!')

