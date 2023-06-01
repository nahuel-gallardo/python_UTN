from Transporte import Transporte

class Auto(Transporte):
    def __init__(self, ruedas, marca, cantidad, velocidad):
        super().__init__(cantidad, velocidad)
        self._ruedas = ruedas
        self._marca = marca

    def frenar(self):
        print("el auto")
        super().frenar()

    def avanzar(self, velocidad):
        print("El auto")
        super().avanzar(velocidad)
    
    def mostrar(self):
        super().mostrar()
        print(f"Cantidad de ruedas:{self._ruedas} - Marca: {self._marca}")
        print("____________________")