''' NAHUEL IAIR GALLARDO 1° B EJERCICIO 2
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”'''

numero_regla = int(input("ingrese un numero del 1 al 8 para conocer la regla correspondiente"))
while numero_regla < 0 or numero_regla > 8:
    numero_regla = int(input("Error.ingrese un numero del 1 al 8 para conocer la regla correspondiente"))

if numero_regla == 1:
    print("21354")
elif numero_regla == 2:
    print("541564")
elif numero_regla == 3:
    print("")
elif numero_regla == 4:
    print("")
elif numero_regla == 5:
    print("")
elif numero_regla == 6:
    print("")
elif numero_regla == 7:
    print("")
else:
    print("")
