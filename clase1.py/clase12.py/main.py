from Transporte import Transporte
from Caballo import Caballo
from Auto import Auto

caballo_1 = Caballo("Andaluz","marron", 2, 20)
caballo_1.set_km_totales(100)

Auto_1 = Auto(4, "fiat", 5, 130)
Auto_1.set_km_totales(500)

otro_auto = Auto(5, "Chevrolet", 6, 200)
otro_auto.set_km_totales(1000)

otro_caballo = Caballo("potro salvaje", "Negro", 4 ,50)
otro_caballo.set_km_totales(300)

caballo_1.avanzar(120)
otro_caballo.avanzar(25)
Auto_1.avanzar(120)
otro_auto.avanzar(210)




lista_transportes = [caballo_1, Auto_1, otro_caballo, otro_auto]


for t in lista_transportes:
    t.mostrar()#POLIMORFISMO

