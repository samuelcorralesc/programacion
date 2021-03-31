from math import pi

r=float(input())
h=float(input())
v=float(input())
m=float(input())
p=pi

vin=p*(r**2)*h
vpar=v*m

vfi=vin-vpar
if vfi>0:
    print(vfi)
else:
    print(0)