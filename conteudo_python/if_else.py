#if / else(se e senão como condição)#
#elif (é a condição dentro da condição)#

nota = int(input('Qual foi a sua nota?'))
if (nota) < 50:
    print('Insuficiente')
elif (nota) < 70:
    print('Suficiente')
elif (nota) < 90:
    print('bom')
else: 
    print('Muito bom')

#adicinado o else em vez de mais um elif
#int atribuido no começo do input para não precisar na estrutura