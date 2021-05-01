cont = 48

texto =  'sollozos somos todos, solos como monos rojos con rostros polvosos'

texto = texto.replace(' ', '')

texto = texto.replace(',', '')

segs = texto.split('o')

for s in segs:

    if s[0] != 's' and s[0] != 'm':

        cont += 3**len(s)

print(cont/2)

 