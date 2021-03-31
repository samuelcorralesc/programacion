x=float(input())
y=float(input())
 
if x<0 and y<0:
     print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 3')

if x>0 and y<0:
     print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 4')

if x<0 and y>0:
     print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 2')

if x>0 and y>0:
     print(f'La coordenada ({x}, {y}) se encuentra en el cuadrante 1')

if x==0 and y==0:
     print(f'La coordenada ({x}, {y}) corresponde al origen')

if x==0 and y!=0:
     print(f'La coordenada ({x}, {y}) esta sobre el eje Y')
     
if y==0 and x!=0:
     print(f'La coordenada ({x}, {y}) esta sobre el eje X')