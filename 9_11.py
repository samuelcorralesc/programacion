def f (x):
    aa=p[0]
    S=p[1]
    C=len(aa)
    N=[]
    G=list(aa)
    W=list(S)
    if not '\n' in  W:
        W.append('\n')
    W.pop()
    for j in range (1,C+1):
        F=G[-1]
        G.pop()
        N.insert(0,F)
        #print(N+G)
        #print(W)
        if (N+G)==W:
            return 1
    return 0 


A=open('f.txt','r')
for ren in A:
    x=ren.split('-')
    Res= f (x)
    if Res==1:
        print ('Es trifelio')
    else:
        print ('No es trifelio')
A.close()