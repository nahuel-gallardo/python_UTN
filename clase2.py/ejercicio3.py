'''NAHUEL IAIR GALLARDO 1° "b"
Ejercicio 03
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)'''

respuesta = "si"
contador_femenino = 0
acumulador_femenino = 0
contador_masculino = 0
mas_joven_voto_nacho = 0 
edad_mas_joven_voto_nacho = 0
contador_nacho = 0
contador_julieta = 0
contador_marcos = 0
contador_votos_gral = 0



while respuesta == "si":

    nombre_votante = input("ingreses su nombre")

    edad_votante = int(input("ingrese su edad"))
    while edad_votante < 13 or edad_votante > 130:
        edad_votante = int(input("Error, edad ingresada incorrecta.ingrese su edad"))

    genero_votante = input("ingrese su genero('f'para femenino, 'm' para masculino,'otro' para otro genero)")
    while genero_votante != "f" and genero_votante != "m" and genero_votante != "otro":
        genero_votante = input("Error.ingrese su genero('f'para femenino, 'm' para masculino,'otro' para otro genero)")

    nombre_participante = input("ingrese el nombre del participante a quien le dara el voto(Nacho, Julieta y Marcos)")
    while nombre_participante != "Nacho" and nombre_participante != "Julieta" and nombre_participante != "Marcos":
        nombre_participante = input("Erros ingrese el nombre del participante (CORRECTAMENTE) a quien le dara el voto(Nacho, Julieta y Marcos)")
    
    if genero_votante == "f":
        contador_femenino = contador_femenino + 1
        acumulador_femenino = acumulador_femenino + edad_votante
    
    if genero_votante == "m" and edad_votante > 24 and edad_votante < 41 and (nombre_participante == "Julieta" or nombre_participante == "Nacho"):
        contador_masculino = contador_masculino + 1

    contador_votos_gral = contador_votos_gral + 1

    match nombre_participante:
        case "Nacho":
            if contador_nacho == 0 or edad_mas_joven_voto_nacho > edad_votante:
                mas_joven_voto_nacho = nombre_votante
                edad_mas_joven_voto_nacho = edad_votante
            else:
                mas_joven_voto_nacho = " nadie voto a nacho"

            contador_nacho = contador_nacho + 1
        case "Julieta":
            contador_julieta = contador_julieta + 1
        case "Marcos":
            contador_marcos = contador_marcos + 1

    respuesta = input("desea continuar votando('si','no')")
if contador_julieta != 0:
    porcentaje_julieta = contador_julieta * 100 / contador_votos_gral
else:
    porcentaje_julieta = "nadie voto a julieta"

if contador_nacho != 0:
    porcentaje_nacho = contador_nacho * 100 / contador_nacho
else:
    porcentaje_nacho = "nadie voto a nacho"
if contador_marcos != 0:
    porcentaje_marcos = contador_marcos * 100 / contador_marcos
else:
    porcentaje_marcos = "nadie voto a nacho"



if contador_marcos > contador_nacho and contador_marcos > contador_julieta:
    ganador = "Marcos"
elif contador_julieta > contador_nacho:
    ganador = "Julieta"
else:
    ganador = "Nacho"




promedio_edad_femenino = acumulador_femenino / contador_femenino

print(f"El promedio de edad de las votantes de género femenino es: " + promedio_edad_femenino)
print(f"Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta." + contador_masculino)
print(f"Nombre del votante más joven que votó a Nacho " + mas_joven_voto_nacho)
print(f"marcos recibio el " + porcentaje_marcos + " de los votos")
print(f"nacho recibio el " + porcentaje_nacho + " de los votos")
print(f"julieta recibio el " + porcentaje_julieta  + " de los votos")
print(f"el ganador es :" + ganador)





