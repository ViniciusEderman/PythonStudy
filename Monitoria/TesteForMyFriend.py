
def cachorro():
    if(codigo == 100):
        produto = "Cachorro-quente"
        preco = 9
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        #print("\n produto: ",produto,"\n preço R$ ",preco,"\n quantidade: ",qtd,"\n total a pagar: R$ ",resut)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
          
def cachorro_duplo():
   if(codigo == 101):
        produto = "Cachorro-quente-duplo"
        preco = 11
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
 
def XEgg():
   if(codigo == 102):
        produto = "X-Egg"
        preco = 12
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))

def XSalada():
   if(codigo == 103):
        produto = "X-Salada"
        preco = 12
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
        
def XBacon():
   if(codigo == 104):
        produto = "X-Bacon"
        preco = 14
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
                
def XTudo():
   if(codigo == 105):
        produto = "X-Tudo"
        preco = 17
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
        
def refrigerante():
   if(codigo == 200):
        produto = "Refrigerante em lata"
        preco = 5
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
        
def chagelado():
   if(codigo == 201):
        produto = "chá gelado"
        preco = 4
        print("você escolheu",produto)
        qtd = int(input("Informe a quantidade -> "))
        resut = (qtd * preco)
        print("\n O produto foi: {} \n Preço: R${:.2f} \n Quantidade: {} \n Total a pagar: R${:.2f} ".format(produto, preco, qtd, resut))
 
#função para pedir mais alguma coisa ou sair do sistema        
def continuarOuParar():
    i = int(input("Inserir outro pedido? \n Digite 1 - para inserir um pedido \n Digite 2 - para não e sair do sistema") )
    if(i == 1):
      print('criar def e chamar esta def para conseguir continuar o somatório de itens sem meu cardapio aparecer dnv e dnv')
      # se atente(Ellen) que se vc sempre chamar uma função, vc retorna quase tudo que está dentro,((sempre retorna seu cardapio))
    else:
        exit("\n \n \n saindo do sistema Delivery Camily Ltda... \n Obrigado, volte sempre!")           

#while True para chamar as funções e executar condições sobre o código que o usuário irá digitar.
def cardapio():
    print ('''
  ------------------------------------------
    Bem-vindo a Lanchonete da Ellen Camily 
  ------------------------------------------
*******CARDÁPIO******
|Código|         Descrição          | Valor |      
| 100  |      Cachorro-quente       |  9,00 |
| 101  |   Cachorro-quente Duplo    | 11,00 |
| 102  |           X-Egg            | 12,00 |
| 103  |          X-Salada          | 12,00 |
| 104  |           X-Bacon          | 14,00 |
| 105  |           X-Tudo           | 17,00 |
| 200  |      Refrigerante Lata     |  5,00 |
| 201  |         Chá Gelado         |  4,00 |
''')


while True:
    #cardapio() //agora funciona de boa. já testei. 2
    
    continuarOuParar()
    codigo = int(input('informe o codigo do produto desejado ->'))  
    if(codigo == 100 ):
      cachorro()
      continuarOuParar()
      continue
    elif(codigo == 101):
        cachorro_duplo()
        continuarOuParar()
    elif(codigo ==102):
        XEgg()
        continuarOuParar()
    elif(codigo ==103):
        XSalada()
        continuarOuParar()
    elif(codigo == 104):
        XBacon()
        continuarOuParar()
    elif(codigo == 105):
        XTudo()
        continuarOuParar()
    elif(codigo == 200):
        refrigerante()
        continuarOuParar()
    elif(codigo == 201):
        chagelado()
        continuarOuParar()
    else:
        print("ops, opção invalida")
        continuarOuParar()
        continue