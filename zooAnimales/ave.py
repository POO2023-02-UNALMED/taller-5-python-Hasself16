from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self.colorPlumas

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        halcon = Ave(nombre, edad, "montanas", genero, "café glorioso")
        return halcon

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        return aguila
