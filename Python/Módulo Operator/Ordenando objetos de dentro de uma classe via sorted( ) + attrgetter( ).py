class Pessoa:
  def __init__(self, nome, idade):
    self.nome = str(nome)
    self.idade = str(idade)
  def __repr__(self):
    return f'{self.nome} {self.idade}'

pessoas = [Pessoa('Ana', 33),
           Pessoa('Carlos', 43),
           Pessoa('Maria', 21),
           Pessoa('Henrique', 90),
           Pessoa('Fernando', 34)]

pessoas_nome = sorted(pessoas, key = lambda obj: obj.nome)

print(pessoas_nome) # Retornará uma lista ordenada por nome

pessoas_idade = sorted(pessoas, key = lambda obj: obj.idade)

print(pessoas_idade) # Retornará uma lista ordenada pela idade

##############################################################

from operator import attrgetter

pessoas_nome = sorted(pessoas, key = attrgetter('nome'))

print(pessoas_nome)# Retornará uma lista ordenada por nome

pessoas_idade = sorted(pessoas, key = attrgetter('idade'))

print(pessoas_idade) # Retornará uma lista ordenada pela idade
