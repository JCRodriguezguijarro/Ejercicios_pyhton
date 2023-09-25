lenguajes=["Python","Java", "Javascript","Kotlin", "C"]

#Estructura for 
for lenguaje in lenguajes:
    print(f"estoy aprendiendo -{lenguaje}")
#En este caso el siguiente print, esta fuera del bucle for, por eso no repite la frase continuamente
print("fuera del bucle for")
#el tercer elemento del parentesis es el incremento de los numeros en la lista
for numero in range(0, 20, 2):
    print(numero)