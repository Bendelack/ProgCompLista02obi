t = int(input())
q = []

for x in range(t):
    num = int(input())
    carneirinhos = input()
    lista = carneirinhos.split(' ')
    distintos = list(set(lista))

    q.append(len(distintos))

for i in q:
    print(i)