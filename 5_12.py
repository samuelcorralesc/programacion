h= int(input())  

u=0                
for i in range(1,h+1):
 n=float(input())
 if i==1:
     x=int(n)
     print(x)

 else:
    u=int(0)
    u=int(n*i-x)
    x=0
    x=n*i
    print(u)