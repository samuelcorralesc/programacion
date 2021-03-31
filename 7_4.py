import math
cantidad=int(input())
y=0

for i in range(cantidad):

  c=299792458 
  v = float(input())
  x=v/3.6
  y=1/math.sqrt(abs(1-x**2/c**2))
  y= "{0:.15f}".format(y) 
  print(y)