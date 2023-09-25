#Whiles siempre que una condicion sea verdadera
#ctrl+k ctrl+c y haces un trozo de codigo comentario
numero =0
while numero <=10:
    print(numero)
    numero +=1 #incremento para evitar un loop infinito

#if dentro while+

numero =0
while numero <=10:
    if numero ==5:
        print("encontramos el numero!!")
        break
else:
    print(numero)
    numero +=1 

    #añadimos el break para ecitar que despues de enconrtrar el 5 no imprima nada por consola