# mi_archivo = open("nombre.txt","w",encoding="utf-8")
# mi_archivo.write("rampi")
# mi_archivo.close()

# mi_archivo = open("nombre.txt","r",encoding="utf-8")
# registro = mi_archivo.read()
# mi_archivo.close()
# print(registro)

# lista = ["Thiago","Gio","Marian","Mario"]
# with open("lista_nombres.txt","w") as mi_archivo:
#     for nombre in lista:
#         mi_archivo.write(f"{nombre}\n")

# mi_archivo = open("lista_nombres.txt","r")
# lista = mi_archivo.readlines()#el readlinesdevuelve una lista
# for line in lista:
#     print(line,end="")

# with open ("lista_nombres.txt","r") as mi_archivo:
#     for line in mi_archivo:
#         print(line,end="")

##ARCHIVO CSV

# nombres = ["thiago","Gio","Marian",]
# apellidos = ["Mujias","Luccheta","Fernandez"]
# edades = [21,23,24]
# TAM = 3
# with open("agenda.csv","w") as archivo:
#     for i in range(TAM):
#         registro = "{0},{1},{2}\n".format(nombres[i],apellidos[i],edades[i])
#         archivo.write(registro)

import re
# with open("agenda.csv","r") as archivo:
#     for line in archivo:
#         #registro = line.split(",")
#         registro = re.split(r",|\n",line)
#         print(f"{registro[0]} - {registro[1]} - {registro[2]}" )



#JSON

import json

# data = {}
# data["alumnos"] = []
# data["alumnos"].append({"nombre":"Juan", "edad":20})
# data["alumnos"].append({"nombre":"Luis", "edad":29})
# data["alumnos"].append({"nombre":"Maria", "edad":32})

# with open("agenda.json","w") as mi_archivo:
#     json.dump(data,mi_archivo,indent = 4)

# with open("agenda.json","r") as mi_archivo:
#     data = json.load(mi_archivo)

# print(data)


# archivo = open("agendita.json","r")
# print(archivo)

def parser_csv(path:str)->list:
    lista = []

    archivo = open(path,"r" , encoding= "utf-8")
    for line in archivo:
        lectura = re.split(",|\n",line)
        print(lectura)

    return lista

lista = parser_csv



