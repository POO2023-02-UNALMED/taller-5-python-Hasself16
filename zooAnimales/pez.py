from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self.colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas

    def getCantidadAletas(self):
        return self.cantidadAletas

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao
