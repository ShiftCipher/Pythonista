# -*- encoding: utf-8 -*-

#ABECEDARIO
abecedario = map(chr, range(97, 123))
index = abecedario.index("n") + 1
abecedario.insert(index, "ñ")
vocales = ["a", "e", "i", "o", "u"]

#DICCIONARIOS
Acciones = ["medir", "comprar", "querer"]
Personales = ['yo','tu','el','nosotros','ustedes','ellos']
Pronombres = ["casa", "apartamento"]
Adjetivos = ["pequeña", "grande"]
Indeterminados = ["un",	"una", "unos", "unas"]
Unidades = ["m2", "Kilometros", "km"]
Condiciones = ["si", "tal vez", "puede ser", "mientras"]

pronombres = [Personales, Acciones, Pronombres, Adjetivos, Indeterminados, Unidades, Condiciones]

#CONJUGACIONES
#FORMAS SIMPLES DEL INDICATIVO

#Presente Indicativo #Presente
TAR = ["o","as","a","amos","áis","an"]
TER = ["o","es","e","emos","éis","en"]
TIR = ["o","es","e","imos","ís","en"]

#Futuro de Indicativo #Futuro
TAR = ["é","ás","á","emos","éis","án"]
TER = ["é","ás","ás","emos","éis","án"]
TIR = ["é","ás","á","emos","éis","án"]

#Preterito Perfecto Simple de Indicativo #Pasado
TAR = ["é","aste","ó","amos","asteis","aron"]
TER = ["í","iste","ió","imos","isteis","ieron"]
TIR = ["í","iste","ió","imos","isteis","ieron"]

#Preterio Imperfecto de Indicativo #Pasado
PIIAR = ["aba","abas","aba","ábamos","abais","aban"]
TER = ["aí","ias","ía","íamos","íais","ían"]
TIR = ["aí","ias","ía","íamos","íais","ían"]

#Condicional Indicativo #Futuro
TAR = ["ía", "ías", "ía", "íamos", "íais", "ían"]
TER = ["ía", "ías", "ía", "íamos", "íais", "ían"]
TIR = ["ía", "ías", "ía", "íamos", "íais", "ían"]


#FORMAS SIMPLES DEL SUBJUNTIVO
#Presente Subjuntivo #Presente
TAR = ["e","es","e","emos","éis","en"]
TER = ["a","as","a","amos","áis","an"]
TIR = ["a","as","a","amos","áis","an"]

#Pretérito Imperfecto de Subjuntivo #Pasado
TAR = ["ara","aras","ara","áramos","arais","aban"]
TER = ["iera","ieras","iera","ieramos","ieras","ieran"]
TIR = ["iera","ieras","iera","ieramos","ieras","ieran"]

#Pretérito Imperfecto de Subjuntivo 2 #Pasado
TAR = ["ase","ases","ase","ásemos","aseis","asen"]
TER = ["iese","ieses","iese","ésemos","ieseis","iesen"]
TIR = ["iese","ieses","iese","ésemos","ieseis","iesen"]

#Futuro de Subjuntivo #Futuro
TAR = ["ere", "ares", "are", "áremos", "areis", "aren"]
TER = ["ere", "ares", "are", "áremos", "areis", "aren"]
TIR = ["ere", "ares", "are", "áremos", "areis", "aren"]


#FORMAS COMPUESTAS DEL INDICATIVO
#Pretérito Perfecto Compuesto de Indicativo #Pasado
Auxiliar = ["he", "has", "ha", "hay", "hemos", "habéis", "han"]
TAR = ["ado"]
TER = ["ido"]
TIR = ["ido"]

#Pretérito Pluscuamperfecto de Indicativo #Pasado
Auxiliar = ["habia", "habias", "habia", "habíamos", "habñiais", "habían"]
TAR = ["ado"]
TER = ["ido"]
TIR = ["ido"]

#Futuro Perfecto de Indicativo #Futuro
Auxiliar = ["habré", "habrás", "habrá", "habremos", "habréis", "habrán"]
TAR = ["ado"]
TER = ["ido"]
TIR = ["ido"]

#Condicional Perfecto de Indicativo #Futuro
Auxiliar = ["habría", "habrías", "habría", "habríamos", "habríais", "habrían"]
TAR = ["ado"]
TER = ["ido"]
TIR = ["ido"]

#Preterito Anterior
Auxiliar = ["hube", "hubiese", "hubo", "hubimos", "hubisteis", "hubieron"]

#FORMAS COMPUESTAS DEL SUBJUNTIVO

#Infinitivo Compuesto
Auxiliar = "haber"

#Pretérito Pluscuamperfecto de Subjuntivo #Pasado
Auxiliar = ["hubiese", "hubieses", "hubieses", "hubiésemos", "hubieseis", "hubiesen"]

#Pretérito Pluscuamperfecto de Subjuntivo 2 #Pasado
Auxiliar = ["hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"]

#Futuro Perfecto #Futuro
Auxiliar = ["hubiere", "hubieres", "hubiere", "hubiéremos", "hubiereis", "hubieren"]

#Gerundio Compuesto
Auxiliar = "Habiendo"

#LIBRERIA
conjugaciones = [Auxiliar, PIIAR, TIR, TAR, TER]

#PRONONMBRES PERSONALES
pppps = ["yo", "me", "mí", "conmigo"]
pppss = ["tú", "te", "ti", "contigo"]
pppts = ["él", "ella", "lo", "la", "le", "se", "sí", "consigo"]
ppppp = ["nosotros", "nosotras", "nos"]
pppsp = ["vosotros", "vosotras", "os"]
ppptp = ["ellos", "ellas", "los", "las", "les"]

#PRONONMBRES DEMOSTRATIVOS
#CERCANIA
pdc = ["este", "esta", "esto", "estos", "estas"]
#DISTANCIA MEDIA
pddm = ["ese", "esa", "eso", "esos", "esas"]
#LEJANIA
pdl = ["aquel", "aquella", "aquello", "aquellos", "aquellas"]

#PRONONMBRES POSESIVOS
#UNICO POSEEDOR
ppup = ["mío", "tuyo", "suyo", "mía", "tuya", "suya"]
#MULTIPLES POSEEDORES
ppmp = ["nuestro", "vuestro", "nuestra", "vuestra"]

#PRONONOMBRES NUMERALES
#CARDINALES
pnc = ["uno", "una"] #Todos los numeros
#ORDINALES
pno = ["primero", "segundo", "primera", "segunda"]
#MULTIPLICATIVOS
pnm = ["doble", "triple"]
#PARTITIVOS
pnp = ["medio"]

#LIBRERIA
diccionario = [pppps, pppss, pppts, ppppp, pppsp, 
		ppptp, pdc, pddm, pdl, ppup, ppmp, pnc, pno,
		pnm, pnp]

verbos = ["Cantare", "Cantabamos", "Canta", "Jugaba"]

verbo = verbos[3]

#SINTAXIS
#Consonantes
def Consonantes():
	consonantes = []
	for letra in abecedario:
		if letra in vocales:
			pass
		else:
			consonantes.append(letra)
	return consonantes
print Consonantes()

#Fonemas
def Fonemas():
	consonantes = Consonantes()
	fonemas = []
	for letra in consonantes:
		for vocal in vocales: 
			fonemas.append(letra + vocal)
	return fonemas
print Fonemas()

#Buscar Verbo Conjugado
def Conjugacion(verbo):
	index = 1
	terminacion = verbo[-index:len(verbo)]

#Buscar Tipo Pronombre 
def Pronombre():
	for grupo in diccionario:
		index = 0
		for elemento in grupo:
			print elemento

# for Persona in zip(singular, plural):
# 	    print Verbo[0:len(Verbo)-2] + terminacion[]

######## REVISAR
singular = {"yo":"primera",
            "tu":"segunda",
			"el":"tercera"}

plural = {"nosotros":"primera",
		"ustedes":"segunda",
		"ellos":"tercera"}

#LEXEMAS

#MORFEMAS

#TIEMPO

#LUGAR

#SENTIMIENTOS

#SENTIDO

#PREDICADO

#SINTAXIS

#PRAGMASIS

#SEMANTICA





