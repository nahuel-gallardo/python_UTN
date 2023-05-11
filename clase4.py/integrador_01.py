#NAHUEL GALLARDO

from data_stark import lista


def mostrar_nombre_masculinos(lista:list):# A
    #mustra el nombre de los personajes maculinos
    #recibe una lista
    for heroe in lista:
        if heroe["genero"] == "M":
            print(heroe["nombre"])

def mostrar_nombres_femeninos(lista:list):#B
    #muestra el nombre de los personajes femeninos
    #recibe una lista
    for heroe in lista:
        if heroe["genero"] == "F":
            print(heroe["nombre"])

def mostrar_mas_alto_masculino(lista:list):#C
    #muestra dentro de los personajes masculinos muestra el mas alto
    #recibe una lista
    lista_hombres = []
    flag_mas_alto = True
    for heroe in lista:
        if heroe["genero"] == "M":
            hombre = {}
            hombre['nombre'] = heroe['nombre']
            hombre['altura'] = heroe['altura']
            lista_hombres.append(hombre)

    for hombre in lista_hombres:
        alturas_hombre_max = float(hombre["altura"])
        if flag_mas_alto == True or alturas_hombre_max > hombre_mas_alta:
            hombre_mas_alta = alturas_hombre_max
            flag_mas_alto = False

    print(f"la altura maxima es {hombre_mas_alta}")

    for hombre in lista_hombres:
        hombre_altura = float(hombre['altura'])
        if hombre_mas_alta == hombre_altura :
            print(f"la hombre mas alto es {hombre['nombre']}")
    
def mostrar_mas_alto_femenino(lista:list):#D
    #muestra dentro de los personajes femeninos el mas alto
    #recibe una lista
    lista_mujeres = []
    flag_mas_alta = True
    for heroe in lista:
        if heroe["genero"] == "F":
            mujer = {}
            mujer['nombre'] = heroe['nombre']
            mujer['altura'] = heroe['altura']
            lista_mujeres.append(mujer)

    for mujer in lista_mujeres:
        alturas_mujer_max = float(mujer["altura"])
        if flag_mas_alta == True or alturas_mujer_max > mujer_mas_alta:
            mujer_mas_alta = alturas_mujer_max
            flag_mas_alta = False

    print(f"la altura maxima es {mujer_mas_alta}")

    for mujer in lista_mujeres:
        mujer_altura = float(mujer['altura'])
        if mujer_mas_alta == mujer_altura :
            print(f"la mujer mas alta es {mujer['nombre']}")

def mostrar_mas_bajo_masculino(lista:list):#E
    #dentro de los personajes masculinos muestra el mas bajo
    #recibe una lista
    lista_hombres = []
    flag_mas_bajo = True
    for heroe in lista:
        if heroe["genero"] == "M":
            hombre = {}
            hombre['nombre'] = heroe['nombre']
            hombre['altura'] = heroe['altura']
            lista_hombres.append(hombre)
        
    for hombre in lista_hombres:
        alturas_hombre_min = float(hombre["altura"])
        if flag_mas_bajo == True or alturas_hombre_min < hombre_mas_bajo:
            hombre_mas_bajo = alturas_hombre_min
            flag_mas_bajo = False
    print(f"la altura minima es {hombre_mas_bajo}")

    for hombre in lista:
        alturas_hombre_min = float(hombre["altura"])
        if alturas_hombre_min == hombre_mas_bajo:
            print(f"el hombre mas bajo es {hombre['nombre']}")

def mostrar_mas_bajo_femenino(lista:list):#F
    #dentro los personajes femeninos muestra el mas bajo
    #recibe una lista
    lista_mujeres = []
    flag_mas_baja = True
    for heroe in lista:
        if heroe["genero"] == "F":
            mujer = {}
            mujer['nombre'] = heroe['nombre']
            mujer['altura'] = heroe['altura']
            lista_mujeres.append(mujer)
        
    for mujer in lista_mujeres:
        alturas_mujer_min = float(mujer["altura"])
        if flag_mas_baja == True or alturas_mujer_min < mujer_mas_baja:
            mujer_mas_baja = alturas_mujer_min
            flag_mas_baja = False
    print(f"la altura minima es {mujer_mas_baja}")

    for mujer in lista:
        alturas_mujer_min = float(mujer["altura"])
        if alturas_mujer_min == mujer_mas_baja:
            print(f"el mujer mas bajo es {mujer['nombre']}")

def mostrar_promedio_altura_masculino(lista:list):#G
    #muestra el promedio de altura de los personajes masculinos
    #recibe una lista
    contador_altura =  0
    acumulador_altura = 0
    lista_hombres = []
    for heroe in lista:
        if heroe["genero"] == "M":
            hombre = {}
            hombre['nombre'] = heroe['nombre']
            hombre['altura'] = heroe['altura']
            lista_hombres.append(hombre)
    for hombre in lista_hombres:
        alturas = float(hombre["altura"])
        acumulador_altura = alturas + acumulador_altura
        contador_altura += 1

    promedio_altura = acumulador_altura / contador_altura

    print(f"el promedio de altura de los heroes es:{promedio_altura}")

def mostrar_promedio_altura_femenino(lista:list):#H
    #muestra el promedio de altura de los personajes femeninos
    #recibe una lista
    contador_altura =  0
    acumulador_altura = 0
    lista_mujeres = []
    for heroe in lista:
        if heroe["genero"] == "F":
            mujer = {}
            mujer['nombre'] = heroe['nombre']
            mujer['altura'] = heroe['altura']
            lista_mujeres.append(mujer)
    for mujer in lista_mujeres:
        alturas = float(mujer["altura"])
        acumulador_altura = alturas + acumulador_altura
        contador_altura += 1

    promedio_altura = acumulador_altura / contador_altura

    print(f"el promedio de altura de los heroes femeninos es:{promedio_altura}")

def mostrar_itemC_itemF(lista:list):#I
    #muestra el punto c y el punto f
    #recibe una lista
    mostrar_mas_alto_masculino(lista)
    mostrar_mas_bajo_femenino(lista)
    mostrar_mas_bajo_masculino(lista)
    mostrar_mas_bajo_femenino(lista)
    

    #listar los herores agrupados por color de ojos

def agrupar_por_color_de_ojos(lista: list, clave:str):#color de ojos
    #agrupa por color de ojos a los personajes
    #recibe una lista y una clave 
    lista_colores = []
    for heroe in lista:
        color_ojos = heroe[clave] 
        lista_colores.append(color_ojos)
    lista_colores_filtrada = set(lista_colores)

    for color in lista_colores_filtrada:
        print(color)
        for heroe in lista:
            if heroe[clave] == color:
                print(f"\t{heroe['nombre']}")

def contar_por_color_de_ojos(lista:list,clave:str):
    #cuenta cuantos personajes hay con cada tipo de color de ojos
    #recibe una lista y una clave
    lista_colores = []
    for heroe in lista:
        color_ojos = heroe[clave] 
        lista_colores.append(color_ojos)
    lista_colores_filtrada = set(lista_colores)

    for color in lista_colores_filtrada:
        contador = 0
        for heroe in lista:
            if heroe[clave] == color:
                contador = contador + 1
        
        print(f"{color}:{contador}")

def agrupar_por_color_de_pelo(lista: list, clave:str):#color de pelo
    #agrupa a los personajes por color de pelo
    #recibe una lista y una clave
    lista_colores = []   
    for heroe in lista:
        color_pelo = heroe[clave] 
        lista_colores.append(color_pelo)
    lista_colores_filtrada = set(lista_colores)

    for color in lista_colores_filtrada:
        print(color)
        color_dic = {color}
        for heroe in lista:
            if heroe[clave] == color:
                print(f"\t{heroe['nombre']}")


def contar_por_color_de_pelo(lista:list,clave:str):
    #cuenta cuantos personajes cada  tipo de color de pelo
    #recibe una lista y una clave
    lista_colores = []
    contador = 0
    for heroe in lista:
        color_pelo = heroe[clave] 
        lista_colores.append(color_pelo)
    lista_colores_filtrada = set(lista_colores)

    for color in lista_colores_filtrada:
        contador = 0
        for heroe in lista:
            if heroe[clave] == color:
                contador = contador + 1
            
        print(f"{color}:{contador}")

def agrupar_por_inteligencia(lista: list, clave:str):#inteligencia
    #determina cuantos superheros tienen cada tipo de inteligancia
    #recibe una lista y una clave
    lista_inteligencia = []
    for heroe in lista:
        tipo_inteligencia = heroe[clave] 
        lista_inteligencia.append(tipo_inteligencia)
    lista_inteligencia_filtrada = set(lista_inteligencia)

    for inteligencia in lista_inteligencia_filtrada:
        print(inteligencia)
        for heroe in lista:
            if heroe[clave] == inteligencia:
                print(f"\t{heroe['nombre']}")
            elif(heroe[clave] == " "):
                print(f"\t{heroe['nombre']} no tiene inteligencia")

def contar_por_inteligencia(lista: list , clave:str):
    #cuenta las cantidad de heroes con cada tipo de inteligencia
    #recibe una lista y una clave
    lista_inteligencia = []
    for heroe in lista:
        tipo_inteligencia = heroe[clave] 
        lista_inteligencia.append(tipo_inteligencia)
    lista_inteligencia_filtrada = set(lista_inteligencia)

    for inteligencia in lista_inteligencia_filtrada:
        
        contador = 0
        for heroe in lista:
            if heroe[clave] == inteligencia:
                contador = contador +1
            elif(heroe[clave] == " "):
                print(f"\t{heroe['nombre']} no tiene inteligencia")
        print(f"{inteligencia}:{contador} ")

menu = ["1.mostrar nombre de los personajes masculinos",
        "2.mostrar nombre de los personajes femeninos",
        "3.calcular cual es el personaje masculino mas alto y mostrar su nombre",
        "4.calcular cual es el personaje femenino mas alto y mostrar su nombre"
        "5.cacular cual es el personaje mas abjo masculino y mostrar su nombre"
        "6.cacular cual es el personaje mas abjo femenino y mostrar su nombre"
        "7.calcular el rpomedio de altura de los personajes masculinos",
        "8.calcular el promedio de altura de los personajes femeninos",
        "9.informar cual es el nombre del superheroe asociado a cada uno de los indicadores anteriores(items C a F)"
        "10.Determinar cuantos superheroes tienen cada tipo de color de ojos",
        "11.Determinar cuantos superheroes tienen cada tipo de color de de pelo",
        "12.Determinar cuantos superheroes tiene cada tipo de ingteligencia",
        "13.Listar todos los superheroes agrupados por color de ojos",
        "14.Listar todos los superheroes agrupados por color de pelo",
        "15.Listar todos los superheroes agrupados por tipo de inteligencia",
        "16.salir del menu"
        ]

seguir = True
while True:
    for opcion in menu:
        print(opcion)
    respuesta = int(input("ingrese una opcion"))
    match respuesta:
        case 1:
            mostrar_nombre_masculinos(lista)
        case 2:
            mostrar_nombres_femeninos(lista)
        case 3:
            mostrar_mas_alto_masculino(lista)
        case 4:
            mostrar_mas_alto_femenino(lista)
        case 5:
            mostrar_mas_bajo_masculino(lista)
        case 6:
            mostrar_mas_bajo_femenino(lista)
        case 7:
            mostrar_promedio_altura_masculino(lista)
        case 8:
            mostrar_promedio_altura_femenino(lista)
        case 9:
            mostrar_itemC_itemF(lista)
        case 10:
            contar_por_color_de_ojos(lista,"color_ojos")
        case 11:
            contar_por_color_de_pelo(lista,"color_pelo")
        case 12:
            contar_por_inteligencia(lista,"inteligencia")
        case 13:
            agrupar_por_color_de_ojos(lista,"color_ojos")
        case 14:
            agrupar_por_color_de_pelo(lista,"color_pelo")
        case 15:
            agrupar_por_inteligencia(lista,"inteligencia")
        case 15:
            break


