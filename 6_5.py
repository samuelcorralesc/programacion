a=[]
b=[]
c=int(input())
d=0 #contador sobrevivientes
for i in range (c):
    x=int(input())
    a+=[x]
a.sort()
for i in range(c):
    x=int(input())
    b+=[x]
b.sort(reverse=True)
for e in range (c):
    if a[e]%2==0 and b[e]%2!=0:
        d+=2
    if b[e]%2==0 and a[e]%2!=0:
        d+=2
print('Sobreviven', d, 'soldados')
