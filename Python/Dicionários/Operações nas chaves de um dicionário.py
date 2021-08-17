alunos = {'Ana':44, 'Carlos':35, 'Thiago':50, 'Isabel':44, 'Tania':18}
professores = {'Carlos':56, 'Fernando':34, 'Rafael':44, 'Tania':60}

print(alunos.keys() & professores.keys()) # Operador & quando aplicado a elementos de um dicionário retornará os elementos que forem comuns aos dois dicionários

# keys suporta operações como em conjuntos, pois os dados das chaves de um dicionário são únicos, logo, é possível aplicar alguns operadores sobre as mesmas. Se tentar aplicar operadores aos values, irá ocorrer um erro pois os dados de values são dinâmicos então não possuem um comportamento padrão definido, haja visto que tais dados moldam seu comportamento de acordo com o tipo de dado atribuido pela sintaxe, que pode sofrer mudança de tipo a qualquer momento.

######################################################################

print(alunos.keys() - professores.keys()) # Retornará quais nomes estão presentes em alunos mas não estão presentes em professores

# Equivalente a diferença entre conjuntos
