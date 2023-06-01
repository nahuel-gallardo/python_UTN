import re
import json
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
            habilidades_sin_espacios = []
            for habilidad in personaje["habilidades"]:
                habilidad_sin_espacios = habilidad.strip()
                habilidades_sin_espacios.append(habilidad_sin_espacios)
            personaje["habilidades"] = habilidades_sin_espacios
        lista_de_diccionarios.append(personaje)
    
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
    return lista_raza_filtrada



def listar_personajes_por_raza(lista:list,clave:str):
    lista_de_raza = []
    for personaje in lista:
        raza = personaje[clave] 
        lista_de_raza.append(raza)
    lista_raza_filtrada = set(lista_de_raza)
    print(lista_raza_filtrada)
    # for raza in lista_raza_filtrada:
    #     print(raza)
    #     for persinaje in lista_de_diccionarios:
    #         if personaje["raza"] == raza:
    #             print(f"{personaje['nombre']},{personaje['poder_de_ataque']}")


listar_personajes_por_raza(lista_de_diccionarios,"raza")