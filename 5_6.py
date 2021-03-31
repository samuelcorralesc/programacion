cantida_lotes = int(input())
longitud_lote_pequeño = float(input())
longitud_incremento  = float(input())
area = 0

# Calculara area:

for i in range(cantida_lotes):
    area = area + (longitud_lote_pequeño)**2
    longitud_lote_pequeño = longitud_incremento + longitud_lote_pequeño
    

print("El area total es de", area, "metros cuadrados")