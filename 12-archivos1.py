#creando y escribiendo datos en un archivo

def app():
    #crear archivo
    archivo =open ("archivo.txt", "w") ##funcion open #w de write, es decir permiso de escritura al archivo, si no existe lo crea en blanco

    #mezclar con 
    for i in range(0, 20):
        archivo.write("Estas en la linea" + str(i) + "\n" )#metodo para escribir un archivo

    archivo.close()
app()