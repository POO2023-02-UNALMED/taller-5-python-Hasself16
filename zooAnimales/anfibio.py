from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPiel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getColorPiel(self):
        return self._colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return salamandra
