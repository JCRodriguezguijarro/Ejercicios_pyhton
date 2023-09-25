lenguajes=["Python","Java", "Javascript","Kotlin", "C"]

#los arrays(list) comienzan en la posicion 0, en este caso 0="python", 4="C".
print(lenguajes[0])

#ordenar alfabeticamente.
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentrod e un texto.
aprendiendos= f"estoy aprendiendo {lenguajes[1]}"
print(aprendiendos)

#Modificar valores de un arrays.
lenguajes[2]="php"

#agregar elementos a un arreglo.
lenguajes.append("C#")
print(lenguajes)

#eliminar de un arrays(list)
del lenguajes[1]
print(lenguajes)

#eliminar con pop una posicion especifica
lenguajes.pop()
print(lenguajes)
#eliminar con pop una posicion especifica
lenguajes.pop(0)
print(lenguajes)
#eliminar por nombre
lenguajes.remove("Python")
print(lenguajes)
