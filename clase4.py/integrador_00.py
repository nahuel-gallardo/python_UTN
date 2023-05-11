from data_stark import lista


def mostrar_nombres_heroes(lista: list):
    #B.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for i in range(len(lista)):
        print(f"{lista[i]['nombre']}")

def mostrar_nombre_altura():
    #C.Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
    #la altura del mismo
    for heroe in lista:
        print(f"{heroe['nombre']}-{heroe['altura']}")

def mostrar_heore_mas_alto():
    #D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_mas_alto = True

    for heroe in lista:
        alturas_heroes_max = float(heroe["altura"])
        if flag_mas_alto == True or alturas_heroes_max > heroe_mas_alto:
            heroe_mas_alto = alturas_heroes_max
            flag_mas_alto = False
            #nombre_heroe_mas_alto = heroe["nombre"]
    print(f"la altura maxima es {heroe_mas_alto}")#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
    #indicadores anteriores (MÁXIMO, MÍNIMO)

    for heroe in lista:
        heroe_mas_altos = float(heroe["altura"])
        if heroe_mas_altos == heroe_mas_alto:
            print(f"el heroe mas alto es: {heroe['nombre']}")

def mostrar_heroe_mas_bajo():
    #MAS BAJO
    flag_mas_bajo = True
    for heroe in lista:
        alturas_heroes_min = float(heroe["altura"])
        if flag_mas_bajo == True or alturas_heroes_min < heroe_mas_bajo:
            heroe_mas_bajo = alturas_heroes_min
            flag_mas_bajo = False
    print(f"la altura minima es {heroe_mas_bajo}")#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
    #indicadores anteriores (MÁXIMO, MÍNIMO)

    for heroe in lista:
        alturas_heroes_min = float(heroe["altura"])
        if alturas_heroes_min == heroe_mas_bajo:
            print(f"el heroe mas bajo es {heroe['nombre']}")

def mostrar_altura_promedio():
    #F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)
    contador_altura =  0
    acumulador_altura = 0
    for heroe in lista:
        alturas = float(heroe["altura"])
        acumulador_altura = alturas + acumulador_altura
        contador_altura += 1

    promedio_altura = acumulador_altura / contador_altura

    print(f"el promedio de altura de los heroes es:{promedio_altura}")

def mostrar_mas_pesado_mas_liviano():

    #H. Calcular e informar cual es el superhéroe más y menos pesado.
    #EL MAS PESADO
    flag_mas_pesado = True
    for heroe in lista:
        peso = float(heroe["peso"])
        if flag_mas_pesado == True or mas_pesado < peso:
            mas_pesado = peso
            flag_mas_pesado = False
    print(f"el mayor peso de los heroes es: {mas_pesado}")

    #LOS MAS PESADOS
    for heroe in lista:
        peso = float(heroe["peso"])
        if peso == mas_pesado:
            print(f"el mas pesado es {heroe['nombre']}")

    flag_menos_pesado = True
    for heroe in lista:
        menor_peso = float(heroe["peso"])
        if flag_menos_pesado == True or menos_pesado > menor_peso:
            menos_pesado = menor_peso
            flag_menos_pesado = False
    print(f"el menor peso de los heroes es: {menos_pesado} ")

    for heroe in lista:
        peso = float(heroe["peso"])
        if menos_pesado == peso:
            print(f"el mas liviano es {heroe['nombre']}")


menu = ["1.Mostrar nombre de cada heroe" , "2.Mostrar nombre y altura de cada heroe","3.Mostrar el heroe mas alto",
        "4.Mostrar el heroe mas bajo","5.Mostrar altura promedio","6.Mostar el heroe mas pesado y el mas liviano","7.Salir"]

#system("cls")

seguir = True
while True:
    for opcion in menu:
        print(opcion)
    respuesta = int(input("ingrese una opcion"))
    match respuesta:
        case 1:
            mostrar_nombres_heroes()
        case 2:
            mostrar_nombre_altura()
        case 3:
            mostrar_heore_mas_alto()
        case 4:
            mostrar_heroe_mas_bajo()
        case 5:
            mostrar_altura_promedio()
        case 6:
            mostrar_mas_pesado_mas_liviano()
        case 7:
            break















        

 


  

  
    



        







