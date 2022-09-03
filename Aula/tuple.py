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

"""
tupla = (1, 2, 3, 4)
for num in tupla:
    print(num)

for indice, valor in enumerate(tupla):
    print(indice, valor)
"""


'contando elementos dentro de uma tupla'
#command .count()

"""
tupla = ("a", "b", "c", "d", "e", "a", "b")
print(tupla.count("c"))

nome = tuple("joaoepedroaranda")
print(nome)
print(nome.count("a"))
"""


'Dicas de utilização'
#command

"""
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez')
#meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez']
#meses.append("mes 13")
print(meses)
"""


'Acessando elementos'
#command

"""
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez')
print(meses[6])
"""


'inteirando com while'
#command

"""
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez')

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
"""


'verificando qual a posição de um elemento na tuple'
#command .index()

"""
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez')

print(meses.index(5))
"""


'Porque usar tuplas'

"""
- são mais rápidas do que listas.
- tuplas deixam seu código mais seguro.(imutabilidade)

"""


'copiando tuple'
#command

tupla = (1, 2, 3)
nova = tupla
