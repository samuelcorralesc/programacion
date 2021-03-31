cromos = []
num = int(input())

while num!=0:
    cromos.append(num)
    num = int(input())

    if num > 682:
        print('Ingrese un número de cromo entre 1 y 682')
        del cromos[-1]
        continue

print(len(set(cromos)))
