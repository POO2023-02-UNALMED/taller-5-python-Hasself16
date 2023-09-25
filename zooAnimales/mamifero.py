from zooAnimales.animal import Animal
class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def isPelaje(self):
        return self.pelaje

    def setPatas(self, patas):
        self.patas = patas

    def getPatas(self):
        return self.patas

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return caballo

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        return leon
