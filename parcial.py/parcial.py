import re
import json
with open("DBZ.csv","r",encoding = "utf-8") as archivo:
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
        contado = f"{raza}:{contador}"
    
    return lista_raza_filtrada


def listar_personajes_por_raza(lista:list,clave:str):
    lista_de_raza = []
    lista_nombre_y_ataque = []
    
    for personaje in lista:
        raza = personaje[clave] 
        lista_de_raza.append(raza)
    lista_filtrada = set(lista_de_raza)
    lista_filtrada_raza = []
    for raza in lista_filtrada:
        lista_filtrada_raza.append(raza)
        # print(f"\n{raza}")
        for personaje in lista:
            if personaje["raza"] == raza:
                personaje = f"\t{personaje['nombre']} - poder de ataque: {personaje['poder_de_ataque']}"
                print(f"\t{personaje['nombre']} - poder de ataque: {personaje['poder_de_ataque']}")

    

def filtrar_por_habilidad_y_raza(habilidad:str,raza:str):
    lista_personajes_filtrados = []
    for personaje in dic_por_raza()[raza]:
      #  print(personaje)
        for tecnica in personaje["habilidades"]:
            if habilidad == tecnica:
                lista_personajes_filtrados.append(personaje)
    return lista_personajes_filtrados




def dic_por_raza():
    lista_raza = contar_por_raza(lista_de_diccionarios,"raza")
    dic_raza = {}
    for raza in lista_raza:
        dic_raza[f"{raza}"] = []
    for personaje in lista_de_diccionarios:
        dic_raza[f"{personaje['raza']}"].append(personaje)
    return dic_raza

def crear_json():
    with open("agenda.json","w") as mi_archivo:
        dict_general = {"lista_de_consultas": []} 
        json.dump(dict_general,mi_archivo,indent = 4)


def cargar_json():
    with open("agenda.json","r") as mi_archivo:
        dict_general = json.load(mi_archivo)
    with open("agenda.json","w") as mi_archivo:
        habilidad_ingresada = input("ingrese una habilidad: ")
        raza_ingresada = input("ingrese una raza: ")
        lista_por_habilidad_y_raza = filtrar_por_habilidad_y_raza(habilidad_ingresada,raza_ingresada)
       # print(lista_por_habilidad_y_raza)
        diccionario_formateado = dic_formato_json(lista_por_habilidad_y_raza,habilidad_ingresada)
        dict_general["lista_de_consultas"].append(diccionario_formateado) 
        json.dump(dict_general,mi_archivo,indent = 4)
    
def dic_formato_json(list_raza_habilidad:list,habilidad_ingesada:str):
    dict_formato = {"personajes":[]}
    for personaje in list_raza_habilidad:
        dic_formato_personaje = {
                                    "nombre": personaje["nombre"],
                                    "poder_de_ataque": personaje["poder_de_ataque"],
                                    "habilidad": personaje["habilidades"].remove(habilidad_ingesada)
            }
        dict_formato["personajes"].append(dic_formato_personaje)
    
    return dict_formato
        

crear_json()

cargar_json()



        
    
            



                
            