def fun(car):
    Ca=len(car)
    P=car[0]
    Cont=0
    for i in range(1,Ca):
        P1=car[i]
        if min(P[0]) > min(P1[0]):
            Cont +=0
        elif min(P[0]) < min(P1[0]):
            Cont +=1
        elif min(P[0]) == min(P1[0]):
            if min(P[1]) > min(P1[1]):
                Cont +=0
            elif min(P[1]) < min(P1[1]):
                Cont +=1
            elif min(P[1]) == min(P1[1]):
                if min(P[2]) > min(P1[2]):
                    Cont +=0
                elif min(P[2]) < min(P1[2]):
                    Cont +=1
                elif min(P[2]) == min(P1[2]):
                    if (P[3]+P[4]+P[5])<(P1[3]+P1[4]+P1[5]):
                        Cont+=1
                    else:
                        Cont+=0
    if Cont==(Ca-1):
         return 1
    return 0     

N=int(input())
for i in range(1, N+1):
    re=input()
    car= re.split( )
    f=fun(car)
    if f==1:
        print('Mi cacharrito es el mas viejo de todos los autos ;D')
    else:
        print('Al menos otro auto es mas viejo que mi cacharrito :(')