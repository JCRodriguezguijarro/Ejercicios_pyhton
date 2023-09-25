def app():

    with open("archivo.txt") as archivo: #por default se abre un txt con  permisos "read"
            for contenido in archivo:
                  print (contenido)# si el txt tiene contenido lo escribe en consola.

app()