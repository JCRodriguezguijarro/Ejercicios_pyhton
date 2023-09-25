 #Agrupas contenido de diferentes tipos de datos.

cancion={     
    "artista" : "Metalica", #llave y valor separados por ":"
    "cancion" : "Enter Sandman",
    "lanzamiento": 1992,
    "visitas" : 294000000
}
print(cancion["visitas"])
print(cancion["lanzamiento"])
print(cancion["cancion"])
print(cancion["artista"])

#mezclar con un string.
#print(f"Estoy escuchando{cancion["artista"]}") [saldria error]

#es aconsejable asignar como variable 

artista = cancion ["artista"]


print(f"Estoy escuchando al mejor grupo de la historia de la musica {artista}")

#agregar nuevos valores
cancion ["playlist"] ="heavy metal"
print(cancion)

#en caso de que exista remplaza el valor
cancion["cancion"]="Seek & Destroy"
print(cancion)


del cancion["lanzamiento"]
print(cancion)



















