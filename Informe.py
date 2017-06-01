# -*- coding: utf-8 -*-

nombre = raw_input("Nombre: ")
tipo = raw_input("1. Raiz, 2.Tuberculos, 3.Platanos: ")
tipo = int(tipo)
corte = raw_input("1. Julianas, 2. Chips, 3.Entero")
corte = int(corte)
cascara = raw_input("¿Cascara? 1.Si, 2.No: ")
cascara = int(cascara)
coccion = raw_input("Seleccione Tipo de Coccion 1.Humeda (Cocinado) 2.Seca (Frito) 3.Mixta: ")
coccion = int(coccion)
peso_inicial = raw_input("Peso Inicial: ")
peso_inicial = float(peso_inicial)
peso_final = raw_input("Peso Final: ")
peso_final = float(peso_final)
tiempo = raw_input("Tiempo: ")
tiempo = int(tiempo)
liquido = raw_input("Liquido: ")
tipo_liquido = ""
resultado = ""
minutos = []
fotos = []
observaciones = []
pregunta = True

while pregunta:
    upload = raw_input("Deseas ingresar mas fotos 1.Si, 2.No: ")
    upload = int(upload)
    if upload == 1:
        minutos.append(raw_input("Ingresa el minuto de la foto: "))
        fotos.append(raw_input("Ingresa la ruta de la foto: "))
        observaciones.append(raw_input("Ingrese la observacion de la foto: "))
    else:
        pregunta = False

if tipo == 1:
    tipo = "la raiz"
if tipo == 2:
    tipo = "el tuberculo"
if tipo == 3:
    tipo = "el platano"

if coccion == 1:
    coccion = "Humeda"
    tipo_liquido = "Agua"
else:
    if coccion == 2:
        coccion = "Seca"
        tipo_liquido = "Aceite de Maiz"
    else:
        coccion = "Mixta"
        tipo_liquido = "Agua y posteriormente en Aceite"

if corte == 1:
    corte = "julianas"
if corte == 2:
    corte = "chips"
if corte == 3:
    corte = "entero"

if peso_final < peso_inicial:
    resultado = "Pierde Peso"
else:
    resultado = "Gana Peso"

if cascara == 1:
    cascara = "con cascara"
else:
    cascara = "sin cascara"

retencion = (peso_final / peso_inicial) * 100
perdida = peso_inicial - peso_final / peso_inicial * 100

print("## " + nombre)

print("""
| Tiempo   |    Foto       |  Observaciones |
|----------|:-------------:|---------------:|""")

for i in range(0, len(fotos)):
    if minutos[i] == "0":
        minutos[i] = "00"
    print("|" + str(minutos[i]) + ":00" "|![Alt text](" + str(fotos[i]) + ")|" + observaciones[i] + "|")


print("\nSe inicia pesando un intercambio de " + nombre +
" equivalente a " + str(int(peso_inicial)) + "g " + cascara +
", se porcionan en " + corte +
" y se llevan a una cocción " + coccion + " durante un tiempo de " + str(tiempo) +
" minutos, en la cual se utilizaron " + liquido + "g de " + tipo_liquido +
", obteniendo un peso final de " + str(int(peso_final)) + "g. Observando que " + tipo +
" " + resultado + "\n")

print("### Porcentaje de retencion\n")

print("|**(Peso final / Peso inicial) * 100**|")
print("|:-----------------------------------:|")
print("|(" + str(peso_final) + " / " + str(peso_inicial) + ") * 100 = " + str("__%.2f" % retencion) + "% de retencion__|\n")

print("### Porcentaje de perdida\n")

print("|**((Peso Inicial – Peso Final)/Peso Inicial)) * 100**|")
print("|:---------------------------------------------------:|")
print("|((" + str(peso_inicial) + " - " + str(peso_final) + ") / " + str(peso_inicial) + ")) * 100 = " + str("__%.2f" % perdida) + "% de perdida__|\n")
