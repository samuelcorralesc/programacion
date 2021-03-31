numero=int(input())
contador=0
 
while True:
	if numero<10:
		break
	numero=numero/2;
	contador+=1
 
print(contador)