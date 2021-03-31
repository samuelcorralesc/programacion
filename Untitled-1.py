f=[]

while True:

    n=int(input())
    f+=[n]

    if n==0:
        break

f.remove(0)
g=max(f)
l=list(range(g+1))
l.remove(0)

for e in l:
    
 
        if e not in f:
    
            print('La ficha faltante es la',e)

