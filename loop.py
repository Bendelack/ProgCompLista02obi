todosOsPicos = []

while True:

    n = int(input())

    if n == 0:
        break

    elif n == 2:
        lista = [int(i) for i in input().split()]
        todosOsPicos.append(2)

    else:


        lista = [int(i) for i in input().split()]
        lista.append(lista[0])
        lista.append(lista[1])

        picosDaOnda = 0

        for i in range(1,(n + 1)):
            if lista[i-1] > lista[i] < lista[i+1] or lista[i-1] < lista[i] > lista[i+1]:
                picosDaOnda += 1

        todosOsPicos.append(picosDaOnda)

for i in todosOsPicos:
    print(i)