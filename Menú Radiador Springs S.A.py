#  define variables
c_rutas=5
c_tipos=3
c_asientos=10
m_asientos=[]
m_tiquetes=[]
m_rutas=[]

# defina valores tiquetes
# 5 filas, 3 cols
m_tiquetes=[[1000,1001,1002],[1100,1101,1102],[1200,1201,1202],[1300,1301,1302],[1400,1401,1402]]

# 5 filas
m_rutas=[ "0. Ruta SJ-Puntarenas","1. Ruta SJ-Limon","2. Ruta SJ-Guanacaste","3. Ruta SJ-Alajuela","4. Ruta SJ-Cartago"]

#1 SUBPROGRAMA PARA COMPRA TIQUETES

def Compre_Tiquetes():
    ruta=int(input("escoja ruta: "))
    asiento=int(input("escoja asiento: "))
    if m_asientos[ruta][asiento]=="d":
        #SI ESTA DISPONIBLE EL ASIENTO
        m_asientos[ruta][asiento]="o"
        tipo=int(input("escoja tipo tiquetes: "))
        print("Compre_Tiquetes")
        print("ruta: ",ruta)
        print("asiento:",asiento)
        print("tipo: ",tipo)
        print("costo de la compra: ",m_tiquetes[ruta][tipo])
    else:
        #NO ESTA DISPONIBLE EL ASIENTO
        print("ruta: ",ruta,",  asiento: ",asiento, "NO disponible")

#2 SUBPROGRAMA inicialice asientos como disponibles
def Inicialice_Asientos_Como_Disponibles():
     print("Inicialice_Asientos_Como_Disponibles")
     for i in range (c_rutas):
        #INICIA LOS ASIENTOS DE UNA FILA CON CONTENIDO NULO 
        fila_de_una_ruta=[]
        for j in range(c_asientos):
            fila_de_una_ruta.append("d")
        m_asientos.append(fila_de_una_ruta)

#3 SUBPROGRAMA desplegue estado de todos los asientos
def Desplegue_Todos_Asientos():
    for i in range (c_rutas):
        for j in range(c_asientos):
            print(m_asientos[i][j],i,j)
        
#4 SUBPROGRAMA desplegue asientos disponibles
def Desplegue_Asientos_Disponibles():
    
    for i in range (c_rutas):
        for j in range(c_asientos):
            if m_asientos[i][j] == 'd':
                print("asiento ",i,j,m_asientos[i][j], " disponible")       

#5 SUBPROGRAMA DESPLEGUE VALORES DE LOS TIQUETES
def Desplegue_Valores_Tiquetes():
    for i in range (c_rutas):
        for j in range(c_tipos):
            print("costo colones: ",m_tiquetes[i][j]," ruta:",i," tipo_tiquete: ",j)
    
#6 SUBPROGRAMA DESPLEGUE RUTAS
def Desplegue_Rutas():
    for i in range(c_rutas):
        print(m_rutas[i])
        

#8 SUBPROGRAMA desplegue el menu
def Desplegue_Menu():
    print("\n"," M e n u","\n")
    print("1. Ver rutas")
    print("2. Ver precios")
    print("3. Adquirir tiquetes")
    print("4. Consultar espacios disponibles")
    print("5. Salir")

# SUBPROGRAMA DESPLEGUE EL MENU
def Desplegue_Menu():
    print('Menu')
    print('1. Ver rutas')
    print('2. Ver precios')
    print('3. Adquirir tiquetes')
    print('4. Consultar espacios disponibles')
    print('5. Salir')

#     i n i c i o   d e l   p r o g r a m a

# llame las partes del proceso
Inicialice_Asientos_Como_Disponibles()
#Asegurase de que entre al while

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
#Grabe archivo plano
print('Fin del programa')
