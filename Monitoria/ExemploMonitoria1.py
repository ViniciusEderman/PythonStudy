variableA = float(input("Digite o valor de A: "))
variableB = float(input("Digite o valor de B: "))
variableC = float(input("Digite o valor de C: "))

if (variableA > variableB) and (variableA > variableC):
    print('o maior valor é: {}'.format(variableA))
elif (variableB > variableA)  and (variableB > variableC):
    print("O maior valor é: ", variableB)
else: 
    print("O maior valor é: ", variableC50)