with open('paise.txt') as archivo:
    lineas=archivo.readlines()
print(lineas)
for l in lineas:
    print(l.replace('rey julien','Antananarivo'))

archivo.close()
