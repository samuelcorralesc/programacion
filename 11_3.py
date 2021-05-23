from random import randint 

Caa=int(input())
Ca=Caa

for i in range (Ca):
    De=int(input())
    A=randint(1,6)
    B=randint(1,6)
    #print(A,B)
    Sa=A+B
    if De==Sa:
        print('Empate')
    elif De>Sa:
        print('Gana la plataforma')
    elif De<Sa:
        print('Gana el humano')