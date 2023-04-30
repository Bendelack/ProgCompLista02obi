n = input()

maior = 0
atual = 0

for x in range(len(n)):
    if n[x] == 'A':
        atual += 1
        if atual > maior:
            maior = atual
    else:
        atual = 0

for x in range(len(n)):
    if n[x] == 'C':
        atual += 1
        if atual > maior:
            maior = atual
    else:
        atual = 0

for x in range(len(n)):
    if n[x] == 'G':
        atual += 1
        if atual > maior:
            maior = atual
    else:
        atual = 0

for x in range(len(n)):
    if n[x] == 'T':
        atual += 1
        if atual > maior:
            maior = atual
    else:
        atual = 0

print(maior)