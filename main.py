import getpass
user = "admin"
password = "admin"

loginCount = 0
opc = 1
opc1= 1

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
    print("\na. Crear Novedad")
    print("b. Modificar Novedad")
    print("c. Eliminar Novedad")
    print("d. Ver Novedades")
    print("e. Volver")

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
        while(opc<1 and opc>5):
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
