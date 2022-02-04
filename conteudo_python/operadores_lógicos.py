#and
#or
#not

#exemplo:

domingo_faz_sol = True
tenho_cachorro = True

if domingo_faz_sol and tenho_cachorro:
    print("vou a praia")
       
#domingo e cachorro = precisam ser V(VERDADEIRA)    

#CASO 02

domingo_faz_sol2 = True
tenho_cachorr2 = False

if domingo_faz_sol2 and tenho_cachorr2:
    print("vou a praia")
else:
    print("fico em casa")

#usando o OR#

ter_dinheiro = False
ser_feliz = False

if ter_dinheiro or ser_feliz:
    print("Tendo dinheiro ou felicidade já é o bastante")
else:
    print("não ter os dois é insuficiente")

#o not inverte a variável de true para f ou f para true#