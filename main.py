import getpass
user = "admin"
password = "admin"

loginCount = 0
opc = 1
opc1= 1
opc3 = 1  # Variable para el submenú 3

# Variables para las novedades

codNovedad1 = 1
textoNovedad1 = "Una novedad importante: Aerolínea XYZ lanza una nueva ruta internacional"
fechaPublicacionNovedad1 = "10/05/2025"
fechaExpiracionNovedad1 = "10/06/2025"

codNovedad2 = 2
textoNovedad2 = "Nueva aerolínea asociada: SkyWings comienza a operar en Argentina"
fechaPublicacionNovedad2 = "12/05/2025"
fechaExpiracionNovedad2 = "12/07/2025"

codNovedad3 = 3
textoNovedad3 = "Mantenimiento programado para el sistema de reservas el día 20/05"
fechaPublicacionNovedad3 = "15/05/2025"
fechaExpiracionNovedad3 = "21/05/2025"

def menu():
    print("\nMenú del Administrador")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")
    print("5. Salir")
    print(" ")
    
def subMenu1():
    global opc1

    while (opc1 != "d"):
        print("\na. Crear Aerolínea")
        print("b. Modificar Aerolínea")
        print("c. Eliminar Aerolínea")
        print("d. Volver")
        
        opc1 = (input("\nIngrese una opción:"))
        while(opc1 != "a" and opc1 != "b" and opc1 != "c" and opc1 != "d"):
            opc1 = (input("Opción inválida. Por favor ingrese una nuevamente:"))
            
        if (opc1=="b" or opc1=="c"):
            construction()
        elif (opc1=="a"):
            createAirline()
                       
def subMenu3():
    global opc3
    
    while (opc3 != "e"):
        print("\na. Crear Novedad")
        print("b. Modificar Novedad")
        print("c. Eliminar Novedad")
        print("d. Ver Novedades")
        print("e. Volver")
        
        opc3 = (input("\nIngrese una opción:"))
        while(opc3 != "a" and opc3 != "b" and opc3 != "c" and opc3 != "d" and opc3 != "e"):
            opc3 = (input("Opción inválida. Por favor ingrese una nuevamente:"))
            
        if (opc3 == "a" or opc3 == "c"):
            construction()
        elif (opc3 == "b"):
            modificar_novedad()
        elif (opc3 == "d"):
            mostrar_novedades()

def subMenu4():
    print("\na. Reporte de Ventas")
    print("b. Reporte de Vuelos")
    print("c. Reporte de Usuarios")
    print("d. Volver")
    
def construction():
    print("\nEn construcción...")
    
def createAirline():
    name = 1
    ARG = 0
    BRA = 0
    CHI = 0
    while (name != "no"):
        name = input("\nIngrese el nombre de una nueva aerolínea, en caso de querer salir ingrese la palabra 'no': ")
        if (name != "no"):
            iata = input("Ingrese código IATA (máx. 3 caracteres): ")
            while (len(iata)>3):
                iata = input("Código inválido. Ingrese código IATA (máx. 3 caracteres): ")
                
            descriptionAirline = input("\nIngrese descripción de la aerolínea: ")
            code = input("\nIngrese el código de país (ARG, BRA O CHI): ")
            if (code =="ARG" or code =="BRA" or code =="CHI"):
                match code:
                    case "ARG":    
                        ARG +=1
                    case "BRA":    
                        BRA +=1
                    case "CHI":    
                        CHI +=1
    
    if (ARG>BRA and ARG>CHI):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Argentina.")
        if (BRA>CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Chile.")
        else:
            print ("El país con menor cantidad de aerolíneas cargadas es Brasil.")
    elif (BRA>ARG and BRA>CHI):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Brasil.")
        if (ARG>CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Chile.")
        else:
            print ("El país con menor cantidad de aerolíneas cargadas es Argentina.")
    elif (CHI>ARG and CHI>BRA):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Chile.")
        if (ARG>BRA):
            print ("El país con menor cantidad de aerolíneas cargadas es Brasil.")
        else:
            print ("El país con menor cantidad de aerolíneas cargadas es Argentina.")      

# Función para mostrar las novedades
def mostrar_novedades():
    print("\nNOVEDADES:")
    print("------------------------------------------")
    
    # Mostrar novedad 1
    print("Código:", codNovedad1)
    print("Texto:", textoNovedad1)
    print("Fecha publicación:", fechaPublicacionNovedad1)
    print("Fecha expiración:", fechaExpiracionNovedad1)
    print("------------------------------------------")
    
    # Mostrar novedad 2
    print("Código:", codNovedad2)
    print("Texto:", textoNovedad2)
    print("Fecha publicación:", fechaPublicacionNovedad2)
    print("Fecha expiración:", fechaExpiracionNovedad2)
    print("------------------------------------------")
    
    # Mostrar novedad 3
    print("Código:", codNovedad3)
    print("Texto:", textoNovedad3)
    print("Fecha publicación:", fechaPublicacionNovedad3)
    print("Fecha expiración:", fechaExpiracionNovedad3)
    print("------------------------------------------")      

# Función para modificar una novedad
def modificar_novedad():
    global textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1
    global textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2
    global textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3
    
    mostrar_novedades()
    
    # Solicitamos el código de la novedad a modificar
    codigo_valido = False
    codigo_a_modificar = 0
    
    while not codigo_valido:
        codigo_ingresado = input("\nIngrese el código de la novedad que desea modificar: ")
        
        # Verificamos si el valor ingresado es un número
        es_numero = True
        for caracter in codigo_ingresado:
            if caracter < '0' or caracter > '9':
                es_numero = False
                break
        
        if es_numero and codigo_ingresado != "":
            codigo_a_modificar = int(codigo_ingresado)
            codigo_valido = True
        else:
            print("Error: El código debe ser un número entero. Intente nuevamente.")
    
    if codigo_a_modificar == codNovedad1:
        print("\nModificando la novedad con código:", codNovedad1)
        
        nuevo_texto = input("Nuevo texto (deje en blanco para mantener el actual): ")
        if nuevo_texto != "":
            textoNovedad1 = nuevo_texto
        
        nueva_fecha_pub = input("Nueva fecha de publicación (deje en blanco para mantener la actual): ")
        if nueva_fecha_pub != "":
            fechaPublicacionNovedad1 = nueva_fecha_pub
        
        nueva_fecha_exp = input("Nueva fecha de expiración (deje en blanco para mantener la actual): ")
        if nueva_fecha_exp != "":
            fechaExpiracionNovedad1 = nueva_fecha_exp
        
    elif codigo_a_modificar == codNovedad2:
        print("\nModificando la novedad con código:", codNovedad2)
        
        nuevo_texto = input("Nuevo texto (deje en blanco para mantener el actual): ")
        if nuevo_texto != "":
            textoNovedad2 = nuevo_texto
        
        nueva_fecha_pub = input("Nueva fecha de publicación (deje en blanco para mantener la actual): ")
        if nueva_fecha_pub != "":
            fechaPublicacionNovedad2 = nueva_fecha_pub
        
        nueva_fecha_exp = input("Nueva fecha de expiración (deje en blanco para mantener la actual): ")
        if nueva_fecha_exp != "":
            fechaExpiracionNovedad2 = nueva_fecha_exp
        
    elif codigo_a_modificar == codNovedad3:
        print("\nModificando la novedad con código:", codNovedad3)
        
        nuevo_texto = input("Nuevo texto (deje en blanco para mantener el actual): ")
        if nuevo_texto != "":
            textoNovedad3 = nuevo_texto
        
        nueva_fecha_pub = input("Nueva fecha de publicación (deje en blanco para mantener la actual): ")
        if nueva_fecha_pub != "":
            fechaPublicacionNovedad3 = nueva_fecha_pub
        
        nueva_fecha_exp = input("Nueva fecha de expiración (deje en blanco para mantener la actual): ")
        if nueva_fecha_exp != "":
            fechaExpiracionNovedad3 = nueva_fecha_exp
        
    else:
        print("No se encontró ninguna novedad con ese código.")
        return
    
    print("\nNovedad modificada con éxito.")



# Programa principal    
while (loginCount<3):
    user1 = input("\nIngrese su usuario: ")
    password1 = getpass.getpass("\nIngrese su contraseña: ")
        
    if (user == user1 and password == password1):
        loginCount = 99
    else: 
        loginCount += 1
        print("\nUsuario y/o contraseña inválido. Reintente nuevamente.")
    
if (loginCount == 3):
    print("Ha fallado 3 intentos. El programa se cerrara.")
else:
    print("¡Ingreso exitoso!")
    
    while (opc!=5):
        menu()
        opc = int(input("\nIngrese una opción: "))
        while(opc<1 or opc>5):  # Corregido el operador de opc>5
            opc = int(input("Opción inválida. Por favor ingrese una nuevamente:"))
        match opc:
            case 1:    
                subMenu1()
            case 2:
                construction()
            case 3:
                subMenu3()
            case 4:
                subMenu4()