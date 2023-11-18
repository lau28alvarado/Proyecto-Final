# SUBPROGRAMA DESPLEGUE EL MENU
def Desplegue_Menu():
    print('Menu')
    print('1. Ver rutas')
    print('2. Ver precios')
    print('3. Adquirir tiquetes')
    print('4. Consultar espacios disponibles')
    print('5. Salir')

opcion = 0 

while opcion <= 4:
    opcion = int(input("Seleccione la opcion\n"))
    if opcion == 1:
        print("Aqui va la opcion 1") 
    elif opcion == 2:
        print("Aqui va la opcion 2")
    elif opcion == 3:
        print("Aqui va la opcion 3" ) 
    elif opcion == 4:
        print("Aqui va la opcion 4" )
    elif opcion == 5:
        print("Aqui va la opcion 5" )
    else:
        print("Escogio opcion erronea:  ",opcion)
        print("Digite opcion 1 a 5")
        opcion = 0
        
print('Aqui va la creacion del archivo plano')
print('Fin del programa')
