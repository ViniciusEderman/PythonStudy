

#dicionário:
#exemplo,

aluno = {
'nome' : 'vinicius',
'idade' : 19,
'vivo' : True,
#podendo adicionar mais coisas 
}

print(aluno)


#vai me resultar um nome, idade e o falor true ou f#


#print específico

print(aluno['idade'])

print(aluno['nome'])

print(aluno['vivo'])

print(aluno.get('nome'))
#formas de buscas, 

#modificando o conteúdo do dicionário

aluno['vivo'] = False
#modificado de t for f


