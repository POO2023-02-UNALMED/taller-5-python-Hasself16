from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil._listado.append(self)

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self.colorEscamas

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola

    def getLargoCola(self):
        return self.largoCola

    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        return iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        return serpiente
