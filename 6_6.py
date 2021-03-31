n=int(input())
m=int(input())
p=[]


for i in range (0,n):
        p.insert(i,0)

for j in range (0,m):
        g=int(input())
        p[g-1]+=1
x=0

for h in range (0,n-1):
        if p[x]<p[h+1]:
                x=h+1
for k in range (0,n):
        if p[k]==p[x] and x!=k and x>k:
                print(k+1)
        elif x==k:
                print(x+1)
        elif p[k]==p[x] and x!=k and x<k:
                print(k+1)
