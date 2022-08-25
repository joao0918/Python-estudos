#nessa seção temos if e else e and or not is
import math

'01'

"""
print("<:> comparação de números <:>")
num_1 = int(input('Insira o 1 número: '))
num_2 = int(input('Insira o 2 número: '))

if num_1 > num_2:
    print(f'O numero {num_1} é maior que o {num_2}')
elif num_2 > num_1:
    print(f'O numero {num_2} é maior que o {num_1}')
else:
    print(f'Os números inseridos são iguais')
"""


'02'

"""
numeroFornecido = int(input('Insira um número qualquer: '))

if numeroFornecido >= 0:
    raizQuadrada = math.sqrt(numeroFornecido) 
    print(f'Raiz quadrada = {raizQuadrada:.2f}')
else:
    print(f'O número inserido({numeroFornecido}) é negativo, por isso ele é invalido no sistema')
"""   


'03'

"""
numeroReal = float(input('INsira um número real: '))

if numeroReal >= 0:
    raizQuadrada = math.sqrt(numeroReal)
    print(f'A raiz de {numeroReal} é {raizQuadrada}')
else:
    quadrado = numeroReal ** 2
    print(f'O quadrado de {numeroReal} é {quadrado}')
"""


'04'

"""
entrada = float(input("insira um número: "))

if entrada >= 0:
    quadrado = entrada ** 2
    print(f'Numero digitado ao quadrado: {quadrado:.2f}')
    raiz = math.sqrt(entrada)
    print(f'Raiz do numero digitado: {raiz:.2f}')
else:
    print('numero digitado é negativo')
"""


'05'

"""
entrada = int(input("Digite um numero inteiro: "))

verificacao = entrada % 2

if verificacao == 1:
    print(f'O numero digitado({entrada}) é impar')
else:
    print(f'O numero digitado({entrada}) é par')
"""


'06'

"""
print('Digite dois numero inteiros: ')

entrada_1 = int(input())
entrada_2 = int(input())

if entrada_1 > entrada_2:
    dif = entrada_1 - entrada_2
    print(f'O numero {entrada_1} é maior que {entrada_2} e a diferença entre eles é de {dif}')
elif entrada_2 > entrada_1:
    dif = entrada_2 - entrada_1
    print(f'O numero {entrada_2} é maior que {entrada_1} e a diferença entre eles é de {dif}')
else: 
    print('Eles são iguais')
"""


'07'

"""
print('Digite dois numero inteiros: ')

entrada_1 = int(input())
entrada_2 = int(input())

if entrada_1 > entrada_2:
    print(f'O numero {entrada_1} é maior que {entrada_2}')
elif entrada_2 > entrada_1:
    print(f'O numero {entrada_2} é maior que {entrada_1}')
else: 
    print('Eles são iguais')
"""


'08'

"""
print(f"Bem-Vindo ao software para calculo de notas, \n digite as duas notas para serem calculadas:")

nota1 = float(input("p1: "))
nota2 = float(input("p2: "))

if nota1 >= 0.0 and nota1 <=10.0:
    if nota2 >= 0.0 and nota2 <=10.0:
        media = (nota1 + nota2) / 2
        print(f"A média desse aluno é: {media:.2f}")
else: 
    print("nota não está no padrão para ser calculada")
"""


'09'

"""
print("Fies, faça uma simulação para aprovação de credito")

salario = float(input("digite quanto vc ganha por mês: R$"))
valor_emprestimo = float(input("Digite o valor do empréstimo que deseja fazer: R$"))
prestacao = int(input(f"Deseja dividir o valor {valor_emprestimo} em quantas vezes: "))
calculo_prestacao = valor_emprestimo / prestacao
verificacao = salario * 0.2
#print(verificacao)
#print(calculo_prestacao)
if calculo_prestacao > verificacao:
    print("Emprestimo concedido")
else:
    print("Emprestimo não concedido")
""" 


'10'

"""
print("calculo peso ideal")

sexo = str(input("Você é homem ou mulher: "))
H = float(input("digit sua altura em metros: "))

if sexo == "homem":
    calculo = (72.7 * H) - 58
    print(f" O peso ideal para sua altura({H}) é {calculo:.2f}")
if sexo == "mulher":
    calculo = (62.1 * H) - 44.7
    print(f" O peso ideal para sua altura({H}) é {calculo:.2f}")
"""
