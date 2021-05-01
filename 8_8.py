def fi (x,ss):
    if (ss.count('ss')==5) or (ss.count('D')==5) or (ss.count('T')==5) or (ss.count('C')==5):
        x.sort()
        if (10 in x) and (11 in x) and (12 in x) and (13 in x) and (14 in x):
            return 1 
        elif (x[0]==x[1]-1) and (x[1]==x[2]-1) and (x[2]==x[3]-1) and (x[3]==x[4]-1):
            return 2
        else:
            return 5
    else:
        x.sort()
        if (x[0]==x[1]-1) and (x[1]==x[2]-1) and (x[2]==x[3]-1) and (x[3]==x[4]-1):
            return 6
        return 0
     


x=[]
ss=[]
Ma=int(input())
for i in range (1,Ma+1):
    for h in range (1,6):
        Ni=int(input())
        L=input()
        x.append(Ni)
        ss.append(L)
    F=fi(x,ss)
    if F==1:
        print('Escalera real')
    elif F==2:
        print('Escalera de color')
    elif F==5:
        print('Color')
    elif F==6:
        print('Escalera normal')
    else:
        print('Otra mano')
    x.clear()
    ss.clear()