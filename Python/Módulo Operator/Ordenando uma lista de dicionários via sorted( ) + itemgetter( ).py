from operator import itemgetter

tabela1 = [{'Nome':'Adriana', 'Idade':26, 'Telefone':991345695},
           {'Nome':'Paulo', 'Idade':67, 'Telefone':984216547},
           {'Nome':'Tania', 'Idade':30, 'Telefone':965457513},
           {'Nome':'Fabricio', 'Idade':18, 'Telefone':999476132},
           {'Nome':'Elisangela', 'Idade':40, 'Telefone':944576125}]

tabela1_pelo_nome = sorted(tabela1, key = itemgetter('Nome'))

print(tabela1_pelo_nome)

tabela1_pela_idade = sorted(tabela1, key = itemgetter('Idade'))

print(tabela1_pela_idade)


###################################################################

tabela1 = [{'Nome':'Adriana', 'Idade':26, 'Telefone':991345695},
           {'Nome':'Paulo', 'Idade':67, 'Telefone':984216547},
           {'Nome':'Tania', 'Idade':30, 'Telefone':965457513},
           {'Nome':'Fabricio', 'Idade':18, 'Telefone':999476132},
           {'Nome':'Elisangela', 'Idade':40, 'Telefone':944576125}]

maior_idade = max(tabela1, key = itemgetter('Idade'))

print(maior_idade)
