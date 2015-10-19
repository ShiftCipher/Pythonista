import random

balotas = []
for numero in range(1,46):
	balotas.append(numero)
print "Balotas: " + str(balotas)

total = 0
for numero in balotas:
	total = total + numero
print "Total: " + str(total)

total = 1
combinaciones = []
for numero in range(40,46):
	combinaciones.append(numero)
	total = total * numero
print "Total Combinaciones: " + str(total)
print "Combinaciones: " + str(combinaciones)

juego = 0
for balota in range(0,7):
	seleccion = random.choice(balotas)
	balotas.remove(seleccion)
	juego = juego + seleccion
print "Juego: " + str(juego)
