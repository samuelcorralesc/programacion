

while True:

    acumulador=0
    contador=0

    n=int(input())

    if n==0:
        break

    for i in range(0,n+1):
        contador+=1
        acumulador+=contador
        if acumulador==n:
            print('Puede ser un racimo ideal')

            break
        elif i==n:
            print('No puede ser un racimo ideal')

