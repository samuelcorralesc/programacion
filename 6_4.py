lista = []
x = int(input())

while x!=0:
    lista.append(x)
    x = int(input())
    lista.sort()

    if x == 0 and len(lista) <= 6:
        print('')
        x = int(input())
        continue

n = len(lista)

if n > 6:
    a = lista[2]
    b = lista[n-3]
    indice =float((b-a)/(n**2))


print(indice)