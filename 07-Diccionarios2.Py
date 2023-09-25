#Iniciamos un diccionario vacio para posteriormente asignar valores

jugador={}
print(jugador)

#se une un jugador a la  partida[IMPORTANTE:cuando lo unicias con valor pones los ":" pero cuando lo asignas despues lo asignas como asignamos una variable]
jugador["nombre"]="Juan"
jugador["puntuacion"]= 0 #no te olvides las comillas por favor juan carlos al declarar
print(jugador)

#incrementando la puntuación
jugador["puntuacion"]= 245
print(jugador)

#acceder a un valor con (get)
print(jugador.get("consola", "no existe ese valor"))

#punteros/iteradores
for llave, valor in jugador.items():
    print(llave)
    print(valor)
#tras abrir un diccionario vacio, hemos añadido un jugador despues, le incrementamos la puntuación, accedemos al valor, y depues interactuamos con el diccionario

#el jugador sale de la partida,eliminamos el jugador y su puntuación 
del jugador["nombre"]
del jugador["puntuacion"]
print(jugador)