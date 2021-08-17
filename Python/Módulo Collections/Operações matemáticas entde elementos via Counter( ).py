from collections import Counter

num1 = ([1,2,2,3,3,3,4,4,4,4])
num2 = ([1,1,2,2,2,2,3,3,3,4])

num3 = num1 + num2 # Irá sequencialmente agrupar os elementos de ambos conjuntos

print(num3)

print(Counter(num3)) # Irá agrupar, de fato como em uma soma, os elementos de num1 com num2, por exemplo, o número 1 (uma ocorrência em num1 e duas ocorrências em num2, resultando 1: 3, equivalente ao resultado 1 = 3 da soma)
