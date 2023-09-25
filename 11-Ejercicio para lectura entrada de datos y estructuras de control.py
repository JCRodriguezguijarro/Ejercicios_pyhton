#ejercicio en el preguntemos a los ususarios, nombramos la playlist, agregar canciones etc desde la terminal.
#notas: intentar dividir el problema en partes mas pequeñas y gestionarlas individualmente para concatenarlas.
#probar cada funcion individualmente 

#creamos un diccionario
playlist = {"nombre": None, "canciones": []}

#funcion para agregar playlist
def app():
    global playlist #importantisimo al añadir playlist como variable global y que este disponible en otras partes del programa.
    agregar_playlist=True

    while agregar_playlist :
        nombre_playlist=input("Como vas a llamar la playlist \r\n")

        if nombre_playlist:
            playlist["nombre"]= nombre_playlist # otra forma de ponerlo. playlist = {"nombre": nombre_playlist}
            agregar_playlist= False #con esto emulamos "brake" ya que al agregar un nombre hacemos que la funcion sea false y no se ejecute el while.
            agregar_canciones()#llamar a la funcion para agregar canciones
 
 #funcion para agregar canciones
def agregar_canciones():
    global playlist
    agregar_cancion= True

    while agregar_cancion:
         nombre_playlist=playlist["nombre"]
         pregunta = f"¿Qué canción quieres agregar a la {playlist['nombre']}? Escribe 'Y' para dejar de agregar canciones: "

         cancion= input(pregunta)
         if cancion.strip().lower() == 'y': #evitamos case sensitivity, esta opcion es mas robusta que if cancion.lower() == 'y':
            break #rompemos bucle infinito
         else:
            playlist["canciones"].append(cancion)
        
#podriamos agregar esta funcion si quitasemos el playlist["canciones"].append(cancion), la funcion se usaria para mostrar el contenido final de la playlist si no quisieramos
#
# def mostrar_resumem():
#     global playlist
#     nombre_playlist= playlist["nombre"]
#     print(f"playlist:{nombre_playlist}\r\n")
#     for cancion in playlist ["canciones"]:
#           print(cancnion)



app()
# Mostrar la playlist final
print(f"Playlist '{playlist['nombre']}':\r\n")
for cancion in playlist['canciones']:
    print(cancion)