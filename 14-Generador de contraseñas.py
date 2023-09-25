

import random
import string
#importamos bibliotecas


#funcion sin argumentos
def generar_contrasena(): 
    longitud = 8  # Longitud fija de la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

contrasena_generada = generar_contrasena()
print("Contraseña generada:", contrasena_generada)