archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas capitales inician con la latra M

lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
    
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
lista=[]
paises=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for q in range(b+2,len(i)):
    lista.append(i[q])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
for i in ciudad:
   if(i[0]=="U"):
    print(i)

#Cuente e imprima cuantos paises que hay en el archivo
lista=[]
cont=0
for i in archivo:
  a=i.index(":")
  cont+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
print(cont)
  
    
#Busque e imprima la ciudad de Singapur
    lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="S") and (i[1]=="i"):
    print(i)
    
#Busque e imprima el pais de Venezuela y su capital
lista=[]
paises=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for q in range(b+2,len(i)):
    lista.append(i[q])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="V")and(i[1]=="e"):
    print(i)
for i in ciudad:
   if(i[0]=="C") and (i[1]=="a") and (i[3]=="a"):
    print(i)

    
#Cuente e imprima las ciudades que su pais inicie con la letra E
lista=[]
paises=[]
ciudad=[]
li=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,len(i)):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    li.append(i)
for i in li:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
    print(i) 

#Buesque e imprima la Capiltal de Colombia
    lista=[]
ciudad=[]

for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]

for i in ciudad:
  if(i[0]=="B") and (i[1]=="o") and (i[2]=="g"):
    print(i)
    
#imprima la posicion del pais de Uganda
archivo= open('paises.txt')
lista=[]
li=[]
a=[]
cont=0
for i in archivo:
  a=i.index(":")
  cont+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  #print(a)
  lista=[]
  li.append(a)
a=li.index('Uganda')
print(a)


#imprima la posicion del pais de Mexico
archivo= open('paises.txt')
lista=[]
li=[]
a=[]
cont=0
for i in archivo:
  a=i.index(":")
  cont+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  #print(a)
  lista=[]
  li.append(a)
a=li.index('México')
print(a)

"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
with open('paise.txt') as archivo:
    lineas=archivo.readlines()
print(lineas)
for l in lineas:
    print(l.replace('rey julien','Antananarivo'))

archivo.close()


#Agregue un país que no esté en la lista(agregar pais "Juan" con capital "David")

with open('paises.txt', 'a') as File:
    File.write('\n')
    File.write('Juan: David')


archivo.close()
