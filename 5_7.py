carga=float(input())
num=int(input())
contador=0
suma=0

for i in range(num):
    peso=float(input())
    suma=suma+peso
    if suma<=carga:
     contador=contador+1

print(contador)
