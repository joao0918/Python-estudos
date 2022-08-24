'listas'
"""
representado por = [arrays]
Entra qualquer tipo de dado [True, 2.1, 2, "joao"]

OBS:
    Dinâmico: Não possui tamanho fixo, e não tem a tipagem...
"""

lista1 = [1, 99, 3, 30, 1, 67, 68, 69]
lista2 = ['j', 'o', 'o', 'o', 'o', 'o', 'a', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('joao pedro')
lista6 = ['joao', 'pedro', 'aranda']
lista7 = [2, 2.4, 'joao', True, 'j', [1, 2, 3]]
cores = ['verde', 'amarelo', 'marron', 'preto']


'check se determinado valor está na lista'
#comando 

"""
if "o" in lista5:
    print('encontrei')
"""


'Ordenação de uma lista'
#comando .sort()

"""
lista1.sort()
print(lista1)
"""


'Contagem de numero de elementos'
#comando .count(valor a contar)

"""
print(f"quantidade de numeros 1 é = {lista1.count(1)}")
"""


'Adicionar um elemento a lista'
#comando .append(valor)

"""
lista1.append(12)
print(lista1)
""" 


'Adicionando vários elementos a lista'
#comando .append([valor, valor])

"""
lista1.append([1, 2, 4])
print(lista1)
"""


'Adicionando vários elementos a lista de outra forma'
#comando .extend([valores,])

"""
lista1.extend([104, 305, 22])
print(lista1)
"""


'Inserindo novo elemento, informado a posição do índice'
#comando .insert(indice, valor)

"""
lista1.insert(3, 2)
print(lista1)
"""


'juntar duas listas'
#comando lista1 + lista 2

"""
lista6 = lista1 + lista2
'ou'
lista1 = lista1 + lista2
print(lista6)
"""


'imprimindo o reverso da lista'
#comando .reverse()

"""
lista1.reverse()
print(lista1)
'mesma coisa'
print(lista1[::-1])
"""


'copiar uma lista'
#comando .copy()

"""
lista6 = lista1.copy()
print(lista6)
"""


'como saber o tamanho da lista'
#comando len(lista)

"""
print(len(lista1))
"""


'removendo o ultimo elemento de uma lista'
#comando .pop() 

"""
lista5.pop()
lista5.pop(2)
print(lista5)
"""


'repetindo elementos em uma lista'
#comando lista1 = lista1 * 3

"""
lista1 = lista1 * 3
print(lista1)
"""


'converter str para uma lista'
#comando var = var.split()

"""
curso = 'joao pedro comeu bala e deu a bunda'
curso = curso.split()
print(curso)
"""


'converter lista para uma str'
#comando var = ' '.join(lista)

"""
#tradução: junte
curso = ''.join(lista2)
print(curso)
"""


'inteirando sobre listas'
#comando for and while

"""
soma = 0
for numeros in lista1:
    print(f"+ {numeros}")
    soma = soma + numeros
    print(soma)


carrinho = []
produto = ''

while produto != 'sim':
    produto = str(input("Adicione um produto ou Digite 'sim' para sair: "))
    if produto != 'sim':
        carrinho.append(produto)
    else:
        print("ok!")

print("os produtos inseridos na sua lista de compras são:")
for produto in carrinho:
    print(produto)    
"""


'acessando elementos de forma indexada'
#comando

"""
#           0         1          2         3
cores = ['verde', 'amarelo', 'marron', 'preto']
print(cores[0])


for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
"""


'Gerar indice em um for'