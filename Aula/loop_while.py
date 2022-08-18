"""
forma geral 

while  expressão_booleana
faça até q seja verdadeiro

numero = False
macaco = 0
while numero == False:
    print(f"teste {macaco}")
    macaco = macaco + 1
    if macaco < 5:
        print(f'entrou {macaco}')
    else:
        numero = True
"""
"""resposta = ''
while resposta != 'sim':
    resposta = input('Termino de estudar?') """

# Saindo do loop com Break, de maneira forçada/projetada. ele pode sair tanto do loop for quanto loop while

for num in range(1,10):
    if num == 6:
        print("irei sair...")
        break
    else:
        print(num)
print("Sai de verdade")
