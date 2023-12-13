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

# función para verificar que los datos digitados sean solo números 
# para que el programa no se interrumpa por 
# ingreso de datos no numéricos
def NumInput(prompt):

    hasta_que_digite_solo_numeros=True                          # para forzar que entre al while y comience a solicitar información al usuario
    while hasta_que_digite_solo_numeros:                        # verifica que deba solicitar al usuario que digite
        hasta_que_digite_solo_numeros=False                     # supone la digitación va a ser de solo números
        cadena=input(prompt+": ")                               # solicita input al usuario
        if len(cadena)==0:                                      # por dado caso si envía cadena vacía
            hasta_que_digite_solo_numeros=True                  # resolicite la información del usuario, en caso de que la cadena esté vacía
        else:
            for c in cadena:                                    # accese cada caracter c digitado por el usuario en cadena 
                if not(c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9"):       # dígitos válidos en cadena
                    hasta_que_digite_solo_numeros=True                                                                          # este caracter no es un dígito
                                                                                                                                # provoca continúe en while hasta_que_digite_solo_numeros
        if hasta_que_digite_solo_numeros==True:                 # pregunta si hubo algún caracter dentro de cadena que no era un dígito
                print("Dato ingresado: ",cadena," no contiene solo números. Por favor Ingrese solo números")                    # porque hubo no dígitos en la cadena de input
    return cadena                                               # sale y retorna lo ingresa, cuando ya el usuariodigite solo números

# Archivo de Factura
# se conserva solo la más reciente factura 
def Crear_Archivo_Plano_Factura(cantidad,tipo_tiquete,subtotal):
    iva_porcentaje=0.13
    iva_monto=subtotal*iva_porcentaje
    total=iva_monto+subtotal
    # se abre para escritura
    Archivo_Plano_Factura=open("Factura.txt","w")
    linea="cantidad="+str(cantidad)+", tipo tiquete= "+str(tipo_tiquete)+", subtotal="+ str(subtotal)
    linea=linea+", iva= "+str(iva_monto)+", total= "+str(total)
    # se graba el detalle de la venta
    Archivo_Plano_Factura.write(linea)
    # se cierra el archivo de detalle de la factura
    Archivo_Plano_Factura.close()

# Archivo de Ventas
# Se conservan todos los montos de las las ventas, sin el IVA
def Crear_Archivo_Plano_Ventas():
    Archivo_Plano_Ventas=open("Almacenar_Todas_Las_Ventas_Realizadas.txt","w")
    Archivo_Plano_Ventas.close()

# cada nueva venta se agrega a las anteriores ventas de la actual ejecución del programa
def Agregar_Ventas_Realizadas(monto_vendido):
    Archivo_Plano_Ventas=open("Almacenar_Todas_Las_Ventas_Realizadas.txt","a")
    linea=str(monto_vendido)+"\n"
    Archivo_Plano_Ventas.write(linea)
    Archivo_Plano_Ventas.close()

# se ejecuta en la opción 5 de salir, ya para finalizar la ejecución del programa    
def Leer_Informacion_del_Archivo_Plano_Ventas():
    recuento_todos_los_montos_vendidos=0

    Archivo_Plano_Ventas=open("Almacenar_Todas_Las_Ventas_Realizadas.txt","r")                      # abrir archivo plano
    # recorrer el archivo plano línea a línea, utilizando la estructura repetitiva for
    for str_monto_vendido in Archivo_Plano_Ventas:                                                  # para accesar total de cada venta
        monto_vendido=int(str_monto_vendido)                                                        # convertir a entero para poder sumarlo
        print("Monto Vendido: ",monto_vendido)                                                      # se imprime el detalle para verificar el total brindado por programa
        recuento_todos_los_montos_vendidos+=monto_vendido                                           # recuento de todos los montos vendidos
    print("El recuento del total de todos los montos vendidos es= ",recuento_todos_los_montos_vendidos)
    Archivo_Plano_Ventas.close()

# Subprograma Para Escoger Números de asiento

def Escoja_Numeros_Asiento(ruta,cantidad_tiquetes_solicitados):
    
    for i in range(1,cantidad_tiquetes_solicitados+1):                              # se cicla hasta obtener todos los tiquetes solicitados
        
        mientras_pida_asiento_valido=True                                           # para cada tiquete, variable que sirve para
                                                                                    # ciclarse hasta obtener un número de asiento válido
        
        while mientras_pida_asiento_valido:                                         # ciclarse hasta obterner un número de asiento válido

            asiento=int(NumInput("escoja asiento: ")) - 1                           # digite el múmero de asiento y ajústelo relativo a cero

            if  0<= asiento and asiento < c_asientos:                               # preguntar si es válido el número de asiento ?
                    
                if m_asientos[ruta][asiento]=="d":                                  # preguntar si está asiento disponible ?
                    #SI ESTA DISPONIBLE EL ASIENTO
                    m_asientos[ruta][asiento]="o"                                   # marque el asiento como ocupado
                    mientras_pida_asiento_valido=False                              # para que solicite siguiente número de asiento,
                                                                                    # porque el actual ya se terminó de procesar
                else:
                    #NO ESTA DISPONIBLE EL ASIENTO
                    print("ruta: ",ruta,",  asiento: ",asiento+1, "NO disponible")  # mensaje si ya el asiento estaba ocupado
            else:
                print("asiento: ",asiento+1," erróneo")                             # mensaje si el número de asiento es erróneo

#1 SUBPROGRAMA PARA venta TIQUETES

def Compre_Tiquetes():
    ruta=int(NumInput("escoja ruta: "))                                             # ingrese ruta
                                          
    if 0 <= ruta and ruta< c_rutas:                                                 # número de la ruta debe ser válido

        tipo=int(NumInput("escoja tipo tiquetes: "))                                # ingrese tipo tiquete
                        
        if 0<=tipo and tipo<c_tipos:                                                # tipo tiquete debe ser válido
            cantidad_asientos_disponibles=Cuente_Cantidad_Asientos_Disponibles(ruta)
            cantidad_tiquetes_solicitados=int(NumInput("Digite la Cantidad de Tiquetes que desea: "))
            
            if  cantidad_tiquetes_solicitados<=cantidad_asientos_disponibles:       # pregunta si hay suficientes asientos disponibles 
                Escoja_Numeros_Asiento(ruta,cantidad_tiquetes_solicitados)          # a interactuar con comprador para escogencia de todos sus asientos
                # regresa aquí ya habiendo escogido todos sus asientos
                print("Venta Tiquetes")
                print("ruta: ",ruta)
                print("tipo: ",tipo)
                print("cantidad tiquetes solicitados: ",cantidad_tiquetes_solicitados)
                monto_vendido=m_tiquetes[ruta][tipo]*cantidad_tiquetes_solicitados
                print("monto de la venta: ",monto_vendido)
                
                # agregar en archivo plano el monto de la venta para almacenar los montos de todas las ventas, esta y las demás
                Agregar_Ventas_Realizadas(monto_vendido)    
                
                # crear archivo plano de la factura de esta venta
                Crear_Archivo_Plano_Factura(cantidad_tiquetes_solicitados,tipo,monto_vendido)
            else:
                print("Cantidad de tiquetes disponibles= ",cantidad_asientos_disponibles, " es menor a los ",cantidad_tiquetes_solicitados, " tiquetes solicitados")
                
        else:
            print("tipo tiquete: ",tipo," erróneo")                                 # si el tipo de tiquete es erróneo      

    else:
        print("ruta: ",ruta," errónea")                                             # si el número de la ruta es erróneo 
        
#2 SUBPROGRAMA inicialice asientos como disponibles, al principio de la corrida
def Inicialice_Asientos_Como_Disponibles():
     print("Inicialice_Asientos_Como_Disponibles")
     for i in range (c_rutas):
        #INICIA LOS ASIENTOS DE UNA RUTA CON CONTENIDO NULO 
        v_fila_de_una_ruta=[]                                                       # inicializar una fila de matriz, correspondiente a los asientos de una Ruta
        for j in range(c_asientos):
            v_fila_de_una_ruta.append("d")                                          # todos los asientos de la Ruta inician disponibles
        m_asientos.append(v_fila_de_una_ruta)                                       # una vez completada la fila de la Ruta, agregarla ya con todos los asientos disponibles 
   
def Cuente_Cantidad_Asientos_Disponibles(ruta):
    cantidad_asientos_disponibles=0
    for j in range(c_asientos):
        if m_asientos[ruta][j] == 'd':                                              # los asientos disponibles están marcados con una "d"
            cantidad_asientos_disponibles+=1 
    return cantidad_asientos_disponibles                                            # funcion que devuelve la cantidad de asientos disponibles de una ruta
            
#4 SUBPROGRAMA desplegue asientos disponibles de una ruta
def Desplegue_Asientos_Disponibles():
    ruta=int(NumInput("escoja ruta: "))
    cantidad_asientos_disponibles=0
                                          
    if 0 <= ruta and ruta< c_rutas:    
        for j in range(c_asientos):
            if m_asientos[ruta][j] == 'd':
                print("ruta: ",ruta,"asiento: ",j+1,m_asientos[ruta][j], " disponible")
                cantidad_asientos_disponibles+=1
        print("\n ruta: ",ruta,", cantidad de asientos disponibles= ",cantidad_asientos_disponibles)
    else:
        print("Ruta= ",ruta," ingresada es errónea")
        

#5 SUBPROGRAMA DESPLEGUE VALORES DE LOS TIQUETES
def Desplegue_Valores_Tiquetes():
    ruta=int(NumInput("escoja ruta: "))
    if 0 <= ruta and ruta< c_rutas: 
        for j in range(c_tipos):
            print("costo colones: ",m_tiquetes[ruta][j]," ruta:",ruta," tipo_tiquete: ",j)
    else:
        print("Número de ruta: ",ruta," es erróneo")
    
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

#     i n i c i o   d e l   p r o g r a m a

# llame las partes del proceso
Inicialice_Asientos_Como_Disponibles()

Crear_Archivo_Plano_Ventas()

#Asegurase de que entre al while
opcion = 0
while opcion <5:
    Desplegue_Menu()   
    opcion = int(NumInput("Seleccione la opcion: "))  
    print("digite opcion: ",opcion,"\n")
    if opcion == 1:
        Desplegue_Rutas()
    elif opcion == 2:
        Desplegue_Valores_Tiquetes()    
    elif opcion == 3:
        Compre_Tiquetes()
    elif opcion == 4:
        Desplegue_Asientos_Disponibles()    
    elif opcion == 5:
        # Para recuento del monto de todas las ventas
        Leer_Informacion_del_Archivo_Plano_Ventas()                                
    else:
        print ("Escogio opción erronea: ",opcion)
        print ("Digite opcion 1 a 5")     
        opcion =0

print('Fin del programa')