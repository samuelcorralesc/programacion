No=int(input())
for i in range(No):

  C=[]

  C1=input()

  for i in range(4):

    L=input().split()
    C.append(L)

  DP=0
  DS=0
  for i in range(len(C)):

    DP+=int(C[i][i])
    DS+=int(C[i][3-i])


  F=[]
  CO=[0,0,0,0]
  for i in range(len(C)):

    X=0
    for a in range(len(C[i])):

      X+=int(C[i][a])
      CO[a]+=int(C[i][a])
    F+=[X]
  S=False

  for i in range(4):
    if F[i]==CO[i]==DP==DS:
      S=True
    else:
      S=False
      break
  if S:
      
    print("Cuadrado magico")
  else:
    print("Cuadrado muggle")