numero = raw_input('Ingrese un numero: ')
numero = int(numero)

while (numero > 0):
	total = numero % 10
	print total
	numero = numero - total 
	numero = numero / 10