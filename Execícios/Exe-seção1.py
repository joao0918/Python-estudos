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

'11'
#k/h para m/s

m_por_s = float(input('Qual a velocidade em KM/H: '))
calculo_kmh = km_por_hora * 3.6
print(f'Valor convertido = {calculo_kmh:.2f}')
"""

'12'

#milhas para km

entrada = float(input('Insira um valor em milhas: '))
saida = 1.61 * entrada
print(f'O valor convertido em KM/H = {saida:.2f}')