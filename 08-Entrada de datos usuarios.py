#funcion input para entrada de datos
nombre=input("Como puedo referirme a ti? \r\n") #\r\n para salta de linea y espaciarlo.

print(f"Encantado de conocerte {nombre}.")

#leer datos que son numeros.
edad=input("Cuantos años tiene usted?")

#si no ponemos no soporta puerto que esta tratando un int como un string(esta comparando 18 en string con 18 en entero)
#declaramosla variable edad a int porque sino trataria a "18" como cadena de texto y no como numero entero
edad= int(edad)
if edad >= 18:
    print("Ya puedes beber alcohol, fumar y votar.\r\n")
else:
    print("Todavia eres muy jover para beber, fumar y votar\r\n")


#mezclarlo con operadores
numero= input("Agrega un numero y te dire si es par o no\r\n")
numero=int(numero)

if numero % 2 == 0:#este modulo nos retorna un numero y si es 0 el numero es par y si fuera 1 el numero seria inpar
    print(f"el numero {numero} es par")
else:
    print(f"el numero{numero} es inpar")

