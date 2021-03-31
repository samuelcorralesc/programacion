import math 
v = float(input("Ingrese la velocidad como factor de c (por ej. 0.85 significa 85% de c):"))
y=1/math.sqrt(1-v**2)
y= "{0:.15f}".format(y) 
print('El factor lorentz es ',y)