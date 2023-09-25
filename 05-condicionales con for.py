lenguajes =["Python", "Kothlin", "Java", "Javascipt","SQL"]


for lenguaje in lenguajes:
    if lenguaje =="Python":
        print("Elegiste un lenguaje muy moderno")
    elif lenguaje=="Java":
        print("Es el lenguaje mas usado actualmente")
    else:
        print(f"{lenguaje} se usan bastante")
#Si Java y python tuviese la misma salida, podemos usar una esctructura or para sintetizar codigo, en este caso si se cumple que sea "Python" o" Java" se usasen muchi usamos el or
# que haga que se cumpla la condicion o usamos else para la otra opcion de salida

for lenguaje in lenguajes:
    if lenguaje == "Python" or lenguaje == "Java":
        print(f"{lenguaje} se usa mucho")
    else:
        print(f"{lenguaje} no se usa tanto")