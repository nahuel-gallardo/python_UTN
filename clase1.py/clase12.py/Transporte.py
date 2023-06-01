class Transporte:
    def __init__(self,cantidad,velocidad):
        self._cantidad_pasajeros = cantidad
        self._velocidad_maxima = velocidad
        self._km_totales = 0
        self._distancia_recorrida = 0

    def avanzar(self,velocidad):
        if velocidad <= self._velocidad_maxima:
            print("esta avanzando")
            self._distancia_recorrida += velocidad
        else:
            print("Atencion... limite de velocidad superado")


    def frenar(self):
        print("esta frenando")
    
    def mostrar(self):
        print(f"**************{type(self)}************")
        print(f"""Cantidad de pasajeros:{self._cantidad_pasajeros} - Velocidad Maxima:{self._velocidad_maxima} 
                - destino: {self.km_totales} - restan:{self.get_distancia()}""")

    def set_km_totales(self, valor):
        self._km_totales = valor
    
    def get_distancia(self):
        return self._km_totales - self._distancia_recorrida