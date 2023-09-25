class Zoologico():
    def __init__(self, nombre=None, ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getNombre(self):
        return(self._nombre)
    
    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getUbicacion(self):
        return self.ubicacion

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self.zonas:
            total += zona.cantidadAnimales()
        return total

    def getZona(self):
        return self.zonas