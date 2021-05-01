from math import factorial

def func(b,a):

    m=len(b)
    d=0

    for ñ in range(0,m):

        q=factorial(int(b[ñ]))

        d=d+q

    if d==a:
        return True
    return False



n=int(input())



li=[]
for i in range(0,n):


    a=int(input())



    b=list(str(a))




    if func(b,a):

        print(a,'es fuerte')




    else:
        print(a,'no es fuerte')




    b.clear()