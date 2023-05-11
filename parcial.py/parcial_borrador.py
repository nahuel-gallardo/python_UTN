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
            personaje["habilidades"] = registro[5].replace("$%"," ").replace("|","").replace(","," ").strip()
            
        lista_de_diccionarios.append(personaje)

def Listar_personajes_por_habilidad(lista:list,valor:list):
    for diccionario in lista:
        if valor == any(diccionario["habilidades"]):   
            print("bhwdqbd")
            promedio = (int(personaje['poder_de_pelea']) + int(personaje['poder_de_ataque'])) / 2 
            print(f"{personaje['nombre']} - {personaje['raza']} - poder promedio: {promedio}")
        else:
            print("esa no existe")
cadena = "      owdqinwdon wikqnodknwqdo    wqodinwqoid    "

print(cadena)