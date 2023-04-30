n = int(input())

lista = []

for x in range(n):
    votos = int(input())
    lista.append(votos)

if lista[0] >= max(lista):
    print('S')
else:
    print('N')