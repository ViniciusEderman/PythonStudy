

#dicionário:
#exemplo,

aluno = {
'nome' : 'vinicius',
'idade' : 19,
'vivo' : True,
#podesse adicionar mais coisa
}

print(aluno)


#vai me resultar nome, idade e o falor true ou f#


#print específico

print(aluno['idade'])

print(aluno['nome'])

print(aluno['vivo'])

print(aluno.get('nome'))
#formas de buscas, 

#modificando o conteúdo do dicionário

aluno['vivo'] = False
#modificado de t for f


