# -*- encoding: utf-8 -*-

algoritmo = "Verbo"

from Conjugaciones import *

#Comando de Voz
Parrafo = "Quiero comprar una casa grande si mide de 100 a 125.5 o 80 m2"
Parrafo = Parrafo.lower()
Parrafo = Parrafo.split()

#Contador de Palabras
def Contador():
	print len(Parrafo)
Contador()

#Busqueda de los tipos
def Busqueda():
	texto = []
	for Palabra in Parrafo:
		if Palabra in Pronombres:
			texto.append(Palabra)

		if Palabra in Indeterminados:
			texto.append(Palabra)

		if Palabra in Adjetivos:
			texto.append(Palabra)

		if Palabra in Acciones:
			print "\t"*2 + Palabra + ": acciones;"

		if Palabra in Unidades:
			texto.append(Palabra)
			return ', '.join(texto)

#Busqueda de Numeros Decimales
def Real():
	for Palabra in Parrafo:
		if Palabra.isalnum() is False:
			#return float(Palabra)
			return str(float(Palabra)) + ": real;"

#Busqueda de Numeros Enteros
def Entero():
	for Palabra in Parrafo:
		if Palabra.isdigit() is True:
			#return int(Palabra)
			return str(int(Palabra)) + ": entero;"

#Busqueda de Condicionales 
def Condicionales():
	for Palabra in Condiciones:
		if Palabra in Parrafo:
			print Parrafo.index(Palabra)
			Index = Parrafo.index(Palabra) + 1
			Comparador = Parrafo[Index]
			if Comparador in Acciones:
				print "Ejecutar"
			return Palabra

#Busqueda de Comparaciones
def Comparaciones():
	pass

#FORMATO

#Declaracion de los Tipos de Datos de las Variables

def main():
	print "algoritmo " + algoritmo + ";"
	print "\tvar"
	print "\t\t" + Busqueda() + ": string;"
	print "\t\t" + Real()
	print "\t\t" + Entero()
	print "\tfvar"
	#Asignacion de los Valores de las Variables
	#Instrucciones
	print "\t\t" + Condicionales()
	print "falgoritmo"

if __name__ == "__main__":
    main()



