def fun(m,n):

    if m==0:
        a=n+1
        return a
    elif m>0 and n==0:
        o=fun(m-1,1)
        return o
    elif m>0 and n>0:
        h=fun(m-1,fun(m,n-1))
        return h

q=int(input())

for i in range(0,q):
    m=int(input())
    n=int(input())

    print(fun(m,n))
