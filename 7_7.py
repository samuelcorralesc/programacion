def multiplo(x):


    if (x%123)==0:

        return 0

    return 1 + multiplo(x+23)


a=int(input())

for u in range(0,a):
    t=int(input())

    print(multiplo(t))

