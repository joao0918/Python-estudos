#nessa seção temos loop for, range, loop while com break

'01'
lista = []
for multiplos in range(0,16,3):
    lista.insert(multiplos,multiplos)   
print(f" todos os multiplos de 3 = {lista}")
