#¿Juan tiene dinero para pagar un coche de 10000 euros?
dinero_juan=947
if dinero_juan <= 10000:
    print("juan es mileurista")
else:
    print("Juan es muy privilegiado")

#ejemplo con lenguajes.
lenguajes_conocidos=3
if lenguajes_conocidos >=5:
    print("Juan sera contratado como programador.")
else:
    print("Juan tiene que seguir esforzandose.")


#IF con texto
lenguajes="Python"
if lenguajes=="Python":
    print("Juan eligio bien el lenguaje")
    
#IF NOT
lenguajes="C#"
if not lenguajes=="Python":
    print("Juan eligio bien el lenguaje")

#Evaluar un boolean.(por ejemplo autentificacion de usuario)
usuario_autentificado =True
if usuario_autentificado:
    print("EL usuario tiene acceso a la información")
else:
    print("Inicie sesión para acceder")

#if elif else(else IF en java)
modelo="Honda"
if modelo=="Kawasaki":
    print(" La moto es verde.")
elif modelo=="Suzuki":
    print("La moto es azul.")
elif modelo=="Honda":
    print("La moto es roja.")
else:
    print("No esta regstrado el modelo de la moto")

#operadores AND y OR.
    #and se tienen que cumplir los dos
usuario_logueado = False
usuario_admin = True 
if usuario_logueado and usuario_admin:
    print("EL usuario es administrador")
elif usuario_logueado and usuario_admin:
    print ("acceso al sistema")
else:
    print("debes iniciar sesión")

    #or al menos se cumple uno
usuario_logueado = False
usuario_admin = True 
if usuario_logueado or usuario_admin:
    print("EL usuario es administrador")
elif usuario_logueado or usuario_admin:
    print ("acceso al sistema")
else:
    print("debes iniciar sesión")

