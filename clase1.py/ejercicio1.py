'''NAHUEL IAIR GALLARDO
Ejercicio 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo ("barbijo", "jabon", "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.'''



tipo = input("ingrese el tipo de producto (barbijo, jabon, alcohol)")
while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
    tipo = input("ingrese el tipo de producto (barbijo, jabon, alcohol)")

precio = float(input("ingrese el precio del producto"))

cantidad_unidades = input("ingrese la cantidad de unidades del producto")

marca = input("ingrese la marca del prodcuto")

fabricante = input("ingrese el nombre del fabricante")

print(tipo)
print(precio)
print(cantidad_unidades)
print(marca)
print(fabricante)



