# def sumar_numeros(primer_numero:int,segundo_numero:int)->int:#implementacion de la funcion

#     suma = primer_numero + segundo_numero

#     return suma


# def restar_numeros(primer_numero:int,segundo_numero:int)->int:
    
#     resta = primer_numero - segundo_numero

#     return resta


# def multiplicar_numeros(primer_numero:int,segundo_numero:int)->None:
#     multiplicacion = primer_numero * segundo_numero
    
#     return multiplicacion
# def dividir_numeros(primer_numero:int,segundo_numero:int)->int:
#     division = None
#     if segundo_numero != 0:
#         division = primer_numero / segundo_numero
#         return division


# while True:
#     opcion = int(input("1.ingresar numeros\n2.restar\n3.Multiplicar\n 4.dividir\n5.sumar. Salir \ningrese una opcion"))

#     match opcion:
#         case 1:
#             x = int(input("ingrese un nunmero: "))
#             y = int(input("ingrese un nunmero: "))
#         case 2:
#             resultado = restar_numeros(x,y)
#             print(f"el resultado de la resta es: {resultado}")
#         case 3:
#             resultado = multiplicar_numeros(x,y)
#             print(f"el resultado de la multiplicacion es: {resultado}")
#         case 4:
#             resultado = dividir_numeros(x,y)
#             if (resultado != None):
#                 print(f"el resultado de la division es: {resultado}")
#             else:
#                 print("el divisor es 0(cero)")
#         case 5:
#             resultado = sumar_numeros(x,y)
#             print(f"el resultado de la suma es: {resultado}")
#         case 6:
#             break