#nessa seção temos if e else e and or not is
import math
"""
'01'
print("<:> comparação de números <:>")
num_1 = int(input('Insira o 1 número: '))
num_2 = int(input('Insira o 2 número: '))

if num_1 > num_2:
    print(f'O numero {num_1} é maior que o {num_2}')
elif num_2 > num_1:
    print(f'O numero {num_2} é maior que o {num_1}')
else:
    print(f'Os números inseridos são iguais')


'02'

numeroFornecido = int(input('Insira um número qualquer: '))

if numeroFornecido >= 0:
    raizQuadrada = math.sqrt(numeroFornecido) 
    print(f'Raiz quadrada = {raizQuadrada:.2f}')
else:
    print(f'O número inserido({numeroFornecido}) é negativo, por isso ele é invalido no sistema')
"""   

'03'

numeroReal = float(input('INsira um número real: '))

if numeroReal >= 0:
    raizQuadrada = math.sqrt(numeroReal)
    print(f'A raiz de {numeroReal} é {raizQuadrada}')
else:
    quadrado = numeroReal ** 2
    print(f'O quadrado de {numeroReal} é {quadrado}')
