No=int(input())
C11=[]
C22=[]
for i in range(No):
  L=input().split()
  C11.append(L)
X=int(input())
for i in range(X):
  L=input().split()
  C22.append(L)
R1=[]
R2=[]
for i in C11:
  for Y in i:
    if Y not in R1:
      R1+=[Y]
for i in C22:
  for Y in i:
    if Y not in R2:
      R2+=[Y]
print("Reggaeton:",len(R1),"Rock:",len(R2))