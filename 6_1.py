h= int(input())  

ran=range(h)
co=0
co1=0
co2=0
co3=0
co4=0
co5=0
num=list(ran)

for i in range(0,h):
    num[i]=int(input())
    if num[i]==1:
     co1=co1+1
    if num[i]==2:
        co2=co2+1
    if num[i]==3:
        co3=co3+1
    if num[i]==4:
        co4=co4+1
    if num[i]==5:
        co5=co5+1

print('1:',co1)
print('2:',co2)
print('3:',co3)
print('4:',co4)
print('5:',co5)
