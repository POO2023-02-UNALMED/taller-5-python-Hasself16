class Zona():
    def __init__(self, nombre=None, zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    
    def setNombre(self,nombre):
        self._nombre=nombre

    def getNombre(self):
        return(self._nombre)
    
    def setZoo(self,zoo):
        self._zoo=zoo

    def getZoo(self):
        return(self._zoo)
    
    def agregarAnimales(self, animal):
        self.animales.append(animal)
        animal.agregarZona(self)

    def cantidadAnimales(self):
        return len(self.animales)