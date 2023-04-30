n = int(input())

info = input().split(' ')
lista = []
for i in info:
    lista.append(int(i))

zeros = 0
ultimo = 0

for i in range(len(lista)):
    if int(lista[i]) == 0 and i > ultimo:
        ultimo = i

valor = 1
repeticoes = (len(lista) - ultimo) - 1
for x in range(repeticoes):
    
    ultimo += 1
    lista.pop(ultimo)
    lista.insert(ultimo, valor)
    valor += 1

for i in lista:

    if int(i) == 0:
        zeros += 1
        if zeros == 1:
            indece = lista.index(i)
            contador = (lista.index(i) - 1)
            valor = 1
            while contador >= 0:
                lista.pop(contador)
                lista.insert(contador, valor)
                contador -= 1
                valor += 1

indexZeros = []

for i in range(len(lista)):
    if lista[i] == 0:
        indexZeros.append(i)

if lista.count(0) > 1:
    for x in range(len(indexZeros) - 1):
        primeiro = indexZeros[x]
        segundo = indexZeros[x+1]
        contador = 0
        
        diferenca = (segundo - 1) - primeiro

        if diferenca % 2 == 0:
            valorIda = 1
            valorVolta = 1

            for x in range(int(diferenca/2)):
                primeiro += 1
                segundo -= 1
                lista.pop(primeiro)
                lista.insert(primeiro, valorIda)
                lista.pop(segundo)
                lista.insert(segundo, valorVolta)
                valorIda += 1
                valorVolta += 1
        else:
            valorIda = 1
            valorVolta = 1

            for x in range(int(diferenca/2)):
                primeiro += 1
                segundo -= 1
                lista.pop(primeiro)
                lista.insert(primeiro, valorIda)
                lista.pop(segundo)
                lista.insert(segundo, valorVolta)
                valorIda += 1
                valorVolta += 1

            primeiro += 1
            lista.pop(primeiro)
            lista.insert(primeiro, valorIda)

for i in range(len(lista)):
    if lista[i] >= 9:
        lista.pop(i)
        lista.insert(i,9)

print(" ".join(str(i) for i in lista))