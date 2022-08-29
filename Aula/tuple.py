'tuplas/tuple' 

#OBS: 1.0
"""
tupla = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5

print(tupla)
print(tupla2)

# 2.0

tupla3 = (1)
tupla4 = (1,)

print(tupla3)
print(type(tupla3))
"""

"""
Podemos ver que tuplas são definidas pela "," e não pelo uso do "()".
"""

'gerando tupla com range'
#command tuple()

"""
tupla = tuple(range(1,10))
print(tupla)
"""


'desempacotando uma tupla'
#command 

"""
tupla = ('joao pedro', 'lindo')

nome, adjetivo = tupla
print(nome, adjetivo)
"""


'adicionando e removendo elementos'

"""
Por serem imutáveis, não existem comandos para adicionar e remover elementos de uma 'tuple'
"""


'soma, máximo, mínimo e tamanho'
#command

"""
tupla = (1, 2, 3, 4, 5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
"""


'concatenar tuples'
#command

"""
tupla = (1, 2, 3, 4)
tupla2 = (6, 7, 8, 9)
soma = tupla + tupla2
print(soma)
"""


'Inteirando uma tupla'
#command

tupla = (1, 2, 3, 4)
for num in tupla:
    print(num)