"""
01
numero = 0
numero = int(input("digite um numero inteiro: "))
print(f"Numero digitado {numero}")

02
NumReal = float(input("Digite um numero real: "))
print(f"Numero real recebido foi --> {NumReal}")

03
print("Digite 3 números inteiros")
Enter1 = int(input("NUMBER 1 ="))
Enter2 = int(input("NUMBER 2 ="))
Enter3 = int(input("NUMBER 3 ="))

soma = Enter1 + Enter2 + Enter3
print(f"Soma dos ter números é igual a {soma}")

04
entrada = float(input("Numero real: "))
quadrado = entrada ** 2
print(f"Numero ao quadrado =  { quadrado:.2f}")

05
quinta = float(input("Numero: "))
div = quinta/5
print(f"a quinta parte {quinta} de é {div:.1f}")

'06'
#Celsius para fahren
  #celcius
valor_recebido = float(input('Insira o valor em celcius: '))
  #Fahren
valor_convertido = (valor_recebido * 1.8) + 32.0

print(f'Valor convertido = {valor_convertido:.1f}')

'07'

#fahren para Celsius

valor_recebido = float(input('Insira o valor em fahren: '))

valor_convertido = 5.0 * (valor_recebido - 32.0)

print(f'Valor convertido = {valor_convertido:.1f}')


'08'
#kelvin para celcius

valor_kelvin = float(input('Insira o valor em kelvin: '))
valor_convertido = valor_kelvin - 273.15
print(f'Valor convertido = {valor_convertido:.2f}')

'09'
#celcius para kelvin

valor_celcius = float(input('Insira o valor em Celcius: '))
valor_convertido = valor_celcius + 273.15
print(f'Valor convertido = {valor_convertido:.2f}')


'10'
#k/h para m/s

km_por_hora = float(input('Qual a velocidade em KM/H: '))
calculo_ms = km_por_hora/3.6
print(f'Valor convertido = {calculo_ms:.2f}')
"""

'11'
#k/h para m/s

"""
m_por_s = float(input('Qual a velocidade em KM/H: '))
calculo_kmh = km_por_hora * 3.6
print(f'Valor convertido = {calculo_kmh:.2f}')
"""


'12'
#milhas para km

"""
entrada = float(input('Insira um valor em milhas: '))
saida = 1.61 * entrada
print(f'O valor convertido em KM/H = {saida:.2f}')
"""

'13'
#km para milhas

"""
entradaK = int(input('insira um valor em quilômetros: '))
conta = entradaK / 1.61
print(f"Resultado convertido em milhas = {conta:.3f}")
"""

'14'
#Ângulo graus para radianos 

"""
pi = 1.14
entradaAngulo = int(input('Valor em ângulo: '))
conta = (entradaAngulo * pi) / 180
print(f"Resultado convertido: {conta:.2f}")
"""


'15'
#Radianos para graus

"""
pi = 1.14
entradaRad = float(input('Valor em Radianos: '))
conta = (entradaRad * 180)/ pi
print(f'Valor convertido: {conta:.2f}')
"""


'16'
#polegadas para centímetros 

"""
entradaPolegadas = int(input('Insira um valor em polegadas: '))
conta = entradaPolegadas * 2.54
print(f'Valor comprimido em centímetros = {conta:.2f}cm')
"""


'17'
# centímetros para polegadas

"""
entradaCm = int(input('Insira um valor em polegadas: '))
conta = entradaCm / 2.54
print(f'Valor polegadas = {conta:.2f}')
"""


'18'
#m3 para litros

"""
entradaCm_3 = float(input('Insira valor em m3: '))
conta = 1000 * entradaCm_3
print(f'Valor em litros: {conta:.2f}')
"""


'19'
#litros para m3

"""
entradaL = float(input('Insira valor em litros: '))
conta = entradaL / 1000
print(f'Valor em Litros: {conta:.2f}')
"""


'20'
#quilogramas para libras

"""
entradaKg = float(input('Insira valor em quilogramas: '))
conta = entradaKg / 0.45
print(f'Valor em libras: {conta:.2f}')
"""


'21'
#libras para quilogramas

"""
entradaLibras = float(input('Insira valor em quilogramas: '))
conta = entradaLibras * 0.45
print(f'Valor em libras: {conta:.2f}')
"""