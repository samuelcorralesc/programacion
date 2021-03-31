h=0

ran=range(h)
ba=0
re=0

num=list(ran)

for i in range(0,h):
    num[i]=int(input())

for j in range(0,h):
    num[j]=int(input())

if num[i]>num[j]:
        ba=ba+2

if num[i]<num[j]:
        re=re+2

if num[i]==num[j]:
        re=re+1
        ba=ba+1


print('el valor es',re)
print('el valor es',ba)