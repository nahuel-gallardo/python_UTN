mi_cadena = "hola"

# print(id(mi_cadena))

# mi_cadena = "despues"


# print(id(mi_cadena))

# mi_cadena = "hola mundo mundo    "
# mi_cadena = mi_cadena.strip()#saca los espacios en blaco a la derecha y a la izquierda de una cadena
# mi_cadena = str(mi_cadena)
# print(mi_cadena)

# #metodo apper

# mi_cadena  = mi_cadena.upper()#todo mayuscula
# mi_cadena = mi_cadena.lower()#todo minuscula
# mi_cadena = mi_cadena.capitalize()#la primer letra mayuscula
# mi_cadena = mi_cadena.replace("mundo","zzz",1)#reemplaza las coinsidencias del primer valor por el segundo en toda la cadena 

# mi_cadena = "Python , Java ,Javascript , C#"
# lista_split = mi_cadena.split(",")# "," -> caracter delimitador,cada vez que se encuentra con ese caracter crea un elmento dentro de una lista
# for lenguaje in lista_split:
#     print(lenguaje.strip())
#print(lista_split)


# separador = "/"
# dia = "10"
# mes = "8"
# año = "2010"
# fecha = separador.join([dia,mes,año])#el join recibe algo iterable como una lista y lo separa con lo que nosotros querramos, en esta caso es 
#                                         #el cual es una barra que separa los valores que estan dentro de los corchetes
# print(fecha)


# cadena = "123"
# cadena = cadena.zfill(5)#rellenar con ceros hacia la izquierda
# print(cadena)


# cadena = "hola mundo"
# print(cadena.isalpha())#devuelve true si es una cadena de alfatica sin espacios



# cadena = "hola1mundo"
# print(cadena.isalnum())#devuelve true si es una cadena alpha numerica


# cadena = "hola mundo"
# print(len(cadena))#devuel el largo de la cadena, si lo usa para una llista devuele la cantidad de elementos de la misma

# cadena = "holalala"
# print(cadena.count("la"))#cuantas veces encuentra "la" dentro de la cadena,sirve para listas de numeros o strings

# cadena = "hola mundo"

# print(cadena[5:10])#rpintea desde el caracter 5 hasta el 10

