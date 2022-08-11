"""
nome = "joao pedro aranda"

for _,valor in enumerate(nome):
    print(valor)

qtd = int(input("quantas vezes esse lop deve rodar"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'informe o valor o {n}/{qtd} valor: '))
    soma = soma + num
print(f"a soma é {soma}")

nome = "joao pedro aranda"
"""
"ele pega oq seria executado e colocado na linha de baixo para, executar e colocar na frente, pois por padrão ele executa e pula uma linha."
"""
for letra in range(0,10):
    print(letra, end="")

for num in range(1,10):
    print("\U0001F60D" * num)
"""
#Range 
"""
range(value_for_stop) --> se n especificar ele iniciara em 0
for num in range(11):
    print(num)
range(value_for_inicio, value_for_stop) --> inicio e parada
for num in range(1, 11):
    print(num)
range(value_for_inicio, value_for_stop, value_for_jump ) --> inicio, parada e de pular de EX(2 em 2)
for num in range(1, 11, 2):
    print(num)    
"""

for num in list(range(10, 0, -1)):
    print(num)  

