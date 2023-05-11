#Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de  autos que tienen disponible a la venta. 
#Para esto se necesita saber de cada auto: la  marca, el año del modelo y el precio (validar los tipos de datos ingresados) y  mostrarlos 
#por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar  listas primero, y despues usando listas y comparar la composición 
#del código. 
#con listas

lista_autos = []

respuesta = "si"

while respuesta == "si":

    marca_auto = input("ingrese la marca del auto ")

    año_modelo = int(input("ingrese el año del modelo del auto" ))
    while año_modelo < 1800 or año_modelo > 2024:
        año_modelo = int(input("Error.Ingreses un año correspondiente "))
    
    precio_auto = int(input("ingrese el precio del auto "))
    while precio_auto < 0:
        precio_auto = int(input("Error.Ingrese un valor valido "))

    autos = {}
    autos["marca"] = marca_auto
    autos["año"] = año_modelo
    autos["precio"] = precio_auto

    lista_autos.append(autos)
        
    respuesta = input("desea ingresar mas datos?(si,no)")

print(lista_autos)







