#uso de un if else dentro de un while
pregunta ="Agrega un numero y te dire si es par o no\r\n"
pregunta += "(Escribe 'cerrar' para salir de la aplicación)\r\n"#+= se usa para concatenar
preguntar =True
while preguntar:
    numero= input (pregunta)

    if numero =="cerrar":
        preguntar=False
    else:
        numero = int(numero)
        if numero % 2 ==0:
            print(f"el numero{numero} es par\r\n")
        else:
            print(f"el numero{numero} es impar\r\n")


#Optimizacion de codigo(de esta forma conseguimos controlar las excepciones, la aplicacion se siga ejecutando aun cuando no pueda cumplir el bucle evitando "ValueError"
# y hacemos que no sea case sensibility)

while True:
    numero = input("Agrega un número y te diré si es par o impar (Escribe 'cerrar' para salir de la aplicación): ")
    #se usa while true para no tener que utilizar "preguntar=False" para salir
    #mostrar el mensaje con el input con las dos "preguntas" para reducir codigo
    if numero.lower() == "cerrar": #esto hace que si por ejemplo ponemos Cerrar con alguna mayus, lo reduzca a minusculas y lo compare evitando case sensitivity.
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")
    except ValueError:
        print("Por favor, ingresa un número válido o 'cerrar' para salir.")
        #value error es para que el programa se siga ejecutando y no pare para mostrar una excepción, de esta forma el bucle se ejecuta y te vuelve a pedir input.