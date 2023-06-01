from Transporte import Transporte

class Caballo(Transporte):
    def __init__(self, raza, color, cantidad, velocidad):
        super().__init__(cantidad, velocidad)
        self._raza = raza
        self._color = color

    def frenar(self):
        print("el caballo")
        super().frenar()

    def avanzar(self,velocidad):
        print("El caballo")
        super().avanzar(velocidad)
    
    def mostrar(self):
        super().mostrar()
        print(f"Raza:{self._raza} - Color{self._color}")
        print("________________")
        