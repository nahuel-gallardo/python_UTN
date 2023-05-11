from data import lista_bzrp
from os import system
system("cls")

#title: BZRP Music Sessions #52
# artista : QUEVEDO  
# views: 227192970 
# length: 204
#img_url: 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
#date:'2022-07-06 00:00:00'


def prueba():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")#cadena es una lista
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba2(titulo:str):
    
    #titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")#cadena es una lista
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba3(titulo:str):
    
    #titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")#cadena es una lista
    if(len(cadena)>1):
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if(len(cadena)>1):
            tipo = cadena2[0].strip()
            numero = cadena2[1].strip()
            print(f"{artista} - {tipo} - {numero}")

def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split("BZRP Music Sessions")
    if(len(parte1)==2):
        artista = parte1[0].replace("||","").strip()
        numero = parte1[1].replace("#","").strip()
        print(f"{artista} - {tipo} - {numero}")


#'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
def url(tema:dict):
    # cadena = tema ["url"].split("=")
    # print(cadena[1])

    #codigo = tema['url'].replace("https://youtube.com/watch?v=","")
    # url = tema['url']


    url = tema['url']
    # l = len("https://youtube.com/watch?v=")
    # codigo = url[l:]#del caracter 28 en adelante(del 'url')
    
    indice = url.index("=")
    codigo = url[indice+1:]
    
    print(codigo)


#date:'2022-07-06 00:00:00'
    
def formatear_fecha(fecha_cadena:str)->str:
    feha_split = fecha_cadena.split(" ")
    fecha = feha_split[0].split("-")
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    seprardor = "/"
    fecha_formato = seprardor.join([dia,mes,año])
    return fecha_formato


    

def test(lista: list):
    for tema in lista:
        fecha = formatear_fecha(tema['date'])
        print(fecha)

def documentacion():
    '''
    Brief:
    Parameters:
    return:
    '''

def mostrar_lista_temas_views():
    #C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
    for tema in lista_bzrp:
        print(f"{tema['title']} - {tema['views']}")

def calcular_maximo(lista:list, clave:str)->int:
    '''
    Brief: Calcula el maximo calor numerico en base a una clave
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        clave: str -> la clave con la cual realizo la busqueda en la lista
    return: un entero que representa el maximo valor de la clave
    '''
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):
        for tema in lista:
            if flag_primero == True or tema[clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    return maximo


def mostrar_lista_temas(lista:list,clave=None,valor=None):
    if clave is None:
        for tema in lista:
            print(f"{tema['title']}")
    else:
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")

def buscar_temas_mas_views(lista:list):
    #D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
    maxima_views = calcular_maximo(lista, "views")
    print(f"Cantidad maxima de reprocciones: {maxima_views}")
    mostrar_lista_temas(lista,'views',maxima_views)     

def buscar_temas_menos_views():
    #E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones(MÍNIMO)
    flag_primero = True
    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] < minima_views:
            minima_views = tema['views']
            flag_primero = False
    print(f"Cantidad minima de reprocciones: {minima_views}")
    for tema in lista_bzrp:
        if tema['views'] == minima_views:
            print(f"{tema['title']}")

def buscar_promedio_views():
    #F. Recorrer la lista y determinar la cantidad total de reproducciones del canal(ACUMULADOR)
    acumulador_views = 0
    for tema in lista_bzrp:
        acumulador_views += tema['views']
    print(f"Sumatoria de reporducciones: {acumulador_views}")

menu = ["1.Mostrar temas",
        "2.Mostrar temas con mas vistas",
        "3.Mostrar temas mas vistos",
        "4.Mostrar temas menos vistos",
        "5.Mostrar promedio de reproducciones",
        "6.Salir"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

def buscar_temas_mas_largo(lista:list):
    maximo_len = calcular_maximo(lista,'length')
    print(f"Duracion maxima: {maximo_len}")
    mostrar_lista_temas(lista,'length',maximo_len)

seguir = True
while seguir == True:

    mostrar_menu()

    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_lista_temas(lista_bzrp)

        case 2:
            buscar_temas_mas_largo(lista_bzrp)

        case 3:
            buscar_temas_mas_views(lista_bzrp)

        case 4:
            buscar_temas_menos_views()

        case 5:
            buscar_promedio_views()

        case 6:
            seguir = False

        case 7:
            test(lista_bzrp)
            

