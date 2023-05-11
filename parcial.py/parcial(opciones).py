import re
import random
from datetime import *
with open("DBZ.csv","r",encoding= "utf-8") as archivo:
    lista_personajes = []
    lista_de_diccionarios = []
    for line in archivo:
        registro = re.split(r",|\n",line)
        lista_personajes.append(registro)       
        for dato in lista_personajes:
            personaje = {}
            personaje["id"] = registro[0]
            personaje["nombre"] = registro[1]
            personaje["raza"] = registro[2]
            personaje["poder_de_pelea"] = registro[3]
            personaje["poder_de_ataque"] = registro[4]
            personaje["habilidades"] = registro[5].strip().split("|$%")
        lista_de_diccionarios.append(personaje)
        #print(personaje["habilidades"][1])


def mostrar_lista_completa(lista:list):
    for diccionario in lista:
        for clave,valor in diccionario.items():
            print(f"{clave} : {valor}")
        print()
        
        

def contar_por_raza(lista: list , clave:str):
    #cuenta las cantidad de heroes con cada tipo de inteligencia
    #recibe una lista y una clave
    lista_de_raza = []
    for personaje in lista:
        raza = personaje[clave] 
        lista_de_raza.append(raza)
    lista_raza_filtrada = set(lista_de_raza)

    for raza in lista_raza_filtrada:
        
        contador = 0
        for personaje in lista:
            if personaje[clave] == raza:
                contador = contador +1
            elif(personaje[clave] == " "):
                print(f"\t{personaje['nombre']} no tiene raza")
        print(f"{raza}:{contador} ")


def listar_personajes_por_raza(lista:list,clave:str):
    lista_de_raza = []
    for personaje in lista:
        raza = personaje[clave] 
        lista_de_raza.append(raza)
    lista_filtrada = set(lista_de_raza)
    lista_filtrada_raza = []
    for raza in lista_filtrada:
        lista_filtrada_raza.append(raza)
        for personaje in lista:
            if personaje["raza"] == raza:
                dict_raza = {}
                dict_raza["nombre"] = personaje["nombre"]
                dict_raza["poder_de_ataque"] = personaje["poder_de_ataque"] 
                lista_filtrada_raza.append(dict_raza)
    print(lista_filtrada_raza)


def Listar_personajes_por_habilidad(lista:list,valor:str):
    for personaje in lista:
        for habilidad in personaje["habilidades"]:
            habilidad.strip()
            if valor == habilidad:
                print("entro")
                promedio = (int(personaje['poder_de_pelea']) + int(personaje['poder_de_ataque'])) / 2 
                dato = f"{personaje['nombre']} - {personaje['raza']} - poder promedio: {promedio}"
                return dato
            else:
                print("esa no existe")

    # for personaje in lista:
    #         if any(valor == habilidad.strip() for habilidad in personaje["habilidades"]):
    #             print("entro")
    #             promedio = (int(personaje['poder_de_pelea']) + int(personaje['poder_de_ataque'])) / 2 
    #             dato = f"{personaje['nombre']} - {personaje['raza']} - poder promedio: {promedio}"
    #             return dato
    #         else:
    #             print("esa no existe")
    
    

#mostrar_lista_completa(lista_de_diccionarios)


def jugar_batalla(nombre:str):
    numero_random = random.randint(0 , 35 ) 
    for personaje in lista_de_diccionarios:
        if nombre == personaje["nombre"]:
            poder_personaje = int(personaje["poder_de_ataque"])
            nombre_1 = personaje["nombre"]
    for personaje in lista_de_diccionarios:
        if numero_random == int(personaje["id"]):
            poder_pc = int(personaje["poder_de_ataque"])
            nombre_pc = personaje["nombre"]
    if poder_pc > poder_personaje:
        ganador = nombre_pc
        perdedor = nombre_1
    else:
        ganador = nombre_1
        perdedor = nombre_pc
    
    fecha = datetime.now().strftime("%x")

    dict_1 = {
        "ganador" : ganador,
        "perdedor": perdedor,
        "fecha" : fecha
    }
    return dict_1



def cargar_archivo():
    with open("ganador_batalla.txt","a",encoding = "utf-8") as archivo_1:
        nombre = input("ingrese el nombre de un personaje: ").capitalize()
        diccionario = str(jugar_batalla(nombre))
        return archivo_1.write(f"\n{diccionario}")
    
#cargar_archivo()
#Listar_personajes_por_habilidad(lista_de_diccionarios,"Summon Majins")




listar_personajes_por_raza(lista_de_diccionarios,"raza")

