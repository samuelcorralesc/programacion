ent=int(input())
l1=[]
for e in range(0,ent):
    v1=input()
    v1=v1.split(', ')
    l1.append(v1)   
l2=[]
for f in l1:
    va=round(float(f[1])/(float(f[2])**2),1)
    if va>25 and float(f[3])>100 and float(f[4])>150:
        ve=[va,f[0]]
        l2.append(ve)
l2.sort(reverse=True)
yo=1
for d in l2:
    print(yo, d[1], d[0] )
    yo+=1