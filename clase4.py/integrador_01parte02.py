
from data_stark import lista

def stark_normalizar_datos(lista:list):
    
    if len(lista) == 0:
        print("error la lista esta vacia")           
    elif len(lista) != 0:
        for heroe in lista:
            contador_modoficaion = 0
            for altura in heroe["altura"]:
                if type(altura) == float:
                    mensaje = "este dato ya es un float"
                elif type(altura) != float:
                    altura = float(heroe["altura"])
                    contador_modoficaion += 1

                if type(heroe["peso"]) == float:
                    mensaje = "este dato ya es un float"
                elif type(heroe["peso"]) != float:
                    peso = float(heroe["peso"])
                    contador_modoficaion += 1
                if type(heroe["fuerza"]) == int:
                    mensaje = "este dato ya es un int"
                elif type(heroe["fuerza"]) != int:
                    fuerza = int(heroe["fuerza"])
                    contador_modoficaion += 1
        print(type(altura))
        print(type(fuerza))
        print(type(peso))
                    
        if contador_modoficaion > 0:
            print("los datos fueron normalizados")   
                    
            


# def lista_vacia(lista:list):
#     return not lista


def obtener_nombre(diccionario:int):
    diccionario = diccionario - 1
    if diccionario >= 0 and diccionario < len(lista):
        nombre = lista[diccionario]["nombre"]
        nombre = f"nombre: {nombre}"
        print(nombre)
    else: 
        print("ese numero de heroe no existe")
    
# nombre_heroe = obtener_nombre(lista,25)

# print(nombre_heroe)
def imprimir_dato(dato:str):
    print(dato)

def stark_imprimir_nombre_heroes(lista:list):
    numero_heroe = 1
    for heroe in lista:
        heroe["nombre"] = obtener_nombre(heroe,numero_heroe)
        numero_heroe += 1
    
    imprimir_dato(lista)


        
# def obtener_nombre_y_dato(diccionario:dato:str,numero_de_heroe:int):
#     numero_de_heroe = numero_de_heroe - 1
#     if numero_de_heroe > 0 and numero_de_heroe < len(lista):
#         nombre = lista[numero_de_heroe]["nombre"]
#         nombre = f"nombre: {nombre}"
#         lista[numero_de_heroe] = {}
#     for 

obtener_nombre(1)