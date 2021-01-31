# coding=utf-8
def crearFacebook():
    def crearFacebook():
        print("<< Cuenta de Facebook >>")
        nombre = input("Nombre del usuario:\n> ")
        edad = int(input("Edad del usuario:\n> "))
        ciudad = input("Ciudad del usuario:\n> ")
        pais = input("Pais del usuario:\n> ")
        correo = input("Correo del usuario:\n> ")
        resumen = ("----Cuenta de Facebook creada----\n"
                   "Nombre del usuario: {nombre}\nEdad del usuario: {edad}\nCiudad del usuario: {ciudad}\n"
                   "Pais del usuario: {pais}\nCorreo del usuario: {correo}\n")
        return resumen

    def crearTwitter():
        print("<< Cuenta de Twitter >>")
        nombre = input("Nombre del usuario:\n> ")
        nombresCompletos = input("Nombres Completos del usuario:\n> ")
        apellidos = input("Apellido Completos del usuario:\n> ")
        edad = int(input("Edad del usuario:\n> "))
        ciudad = input("Ciudad del usuario:\n> ")
        pais = input("Pais del usuario:\n> ")
        idioma = input("Idioma del usuario:\n> ")
        correo = input("Correo electronico del usuario:\n> ")
        print("----Cuenta de Twitter creada----\n"
              "Nombre del usuario: {nombre}\nNombres Completos del usuario: {nombresCompletos}\nApellidos "
              "Completos del usuario: {apellidos}\nEdad del usuario: {edad}\n"
              "Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nIdioma del usuario: {idioma}\n"
              "Correo del usuario: {correo}\n")

    def crearWhatsapp():
        print("<< Cuenta de Whatsapp >>")
        nombre = input("Nombre del usuario:\n> ")
        numero = int(input("Telefono del usuario:\n> "))
        edad = int(input("Edad del usuario:\n> "))
        ciudad = input("Ciudad del usuario:\n> ")
        pais = input("Pais del usuario:\n> ")
        resumen = ("----Cuenta de Whatsapp creada----\n"
                   "Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
                   "Edad del usuario: {edad}\nCiudad del usuario: {ciudad}\nPais del usuario: {pais}\n")
        return resumen

    def crearTelegram():
        print("<< Cuenta de Telegram >>")
        nombre = input("Nombre del usuario:\n> ")
        numero = int(input("Telefono del usuario:\n> "))
        ciudad = input("Ciudad del usuario:\n> ")
        pais = input("Pais del usuario:\n> ")
        interes = input("Area de interés del usuario:\n> ")
        print("----Cuenta de Telegram creada----\n"
              "Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
              "Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nArea de interés del usuario: {interes}\n")

    def crearSignal():
        print("<< Cuenta de Signal >>")
        nombre = input("Nombre del usuario:\n> ")
        numero = int(input("Telefono del usuario:\n> "))
        ciudad = input("Ciudad del usuario:\n> ")
        pais = input("Pais del usuario:\n> ")
        hobby = input("Hobby principal del usuario:\n> ")
        resumen = ("----Cuenta de Signal creada----\n"
                   "Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
                   "Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nHobby principal del usuario: {hobby}\n")
        return resumen

    def crearInstagram():
        print("<< Cuenta de Instagram >>")
        nombre = input("Nombre del usuario:\n> ")
        ciudad = input("Ciudad del usuario:\n> ")
        edad = int(input("Edad del usuario:\n> "))
        correo = input("Correo del usuario:\n> ")
        print("----Cuenta de Instagram creada----\n"
              "Nombre del usuario: {nombre}\nCiudad del usuario: {ciudad}\nEdad del usuario: {edad}\n"
              "Correo del usuario: {correo}\n")

    def crearFlickr():
        print("<< Cuenta de Flickr >>")
        nombre = input("Nombre del usuario:\n> ")
        correo = input("Correo del usuario:\n> ")
        resumen = ("----Cuenta de Flickr creada----\n"
                   "Nombre del usuario {nombre}\nCorreo del usuario: {correo}\n")
        return resumen

    def obtenerMensaje(cuentasCreadas):
        mensaje = ""
        mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
        if (cuentasCreadas >= 1) and (cuentasCreadas <= 5):
            mensaje = mensajeFinal[0]
        elif (cuentasCreadas >= 6) and (cuentasCreadas <= 15):
            mensaje = mensajeFinal[1]
        elif cuentasCreadas >= 16:
            mensaje = mensajeFinal[2]
        return mensaje

    if __name__ == "__main__":
        bandera = True
        contador = 0
        while bandera:
            opcion = int(input("Ingrese 1 si desea crear una cuenta de Facebook\n"
                               + "Ingrese 2 si desea crear una cuenta de Twitter\n"
                               + "Ingrese 3 si desea crear una cuenta de Whatsapp\n"
                               + "Ingrese 6 si desea crear una cuenta de Telegram\n"
                               + "Ingrese 5 si desea crear una cuenta de Signal\n"
                               + "Ingrese 6 si desea crear una cuenta de Instagram\n"
                               + "Ingrese 7 si desea crear una cuenta de Flickr\n> "))
            if opcion == 1:
                print(crearFacebook())
            elif opcion == 2:
                crearTwitter()
            elif opcion == 3:
                print(crearWhatsapp())
            elif opcion == 4:
                crearTelegram()
            elif opcion == 5:
                print(crearSignal())
            elif opcion == 6:
                crearInstagram()
            elif opcion == 7:
                print(crearFlickr())
            else:
                print("No es una opcion a seleccionar")
            contador = contador + 1
            salida = int(input("Ingrese el numero 1 si desea salir del ciclo\n> "))
            if salida == 1:
                bandera = False
        print("La campaña es una: " + obtenerMensaje(contador))