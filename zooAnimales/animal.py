from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.anfibio import Anfibio

class Animal():
    totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        Animal.totalAnimales+=1
        self._zona=[]
    
    def setNombre(self, nombre):
        self._nombre=nombre

    def getNombre(self):
        return (self._nombre)
    
    def setEdad(self, edad):
        self._edad=edad

    def getEdad(self):
        return (self._edad)
    
    def setHabitat(self, habitat):
        self._habitat=habitat

    def getHabitat(self):
        return (self._habitat)
    
    def setGenero(self, genero):
        self._genero=genero
    
    def getGenero(self):
        return (self._genero)
    
    def agregarZona(self, zona):
        self._zona.append(zona)

    @staticmethod
    def totalPorTipo():
        return (
            "Mamiferos: "
            + str(Mamifero.cantidadMamiferos())
            + "\n"
            + "Aves: "
            + str(Ave.cantidadAves())
            + "\n"
            + "Reptiles: "
            + str(Reptil.cantidadReptiles())
            + "\n"
            + "Peces: "
            + str(Pez.cantidadPeces())
            + "\n"
            + "Anfibios: "
            + str(Anfibio.cantidadAnfibios())
        )

    def __str__(self):
        if not self.zona:
            print(
                "Mi nombre es "
                + self.getNombre()
                + ", tengo una edad de "
                + str(self.getEdad())
                + ", habito en "
                + self.getHabitat()
                + " y mi genero es "
                + self.getGenero()
            )
            return (
                "Mi nombre es "
                + self.getNombre()
                + ", tengo una edad de "
                + str(self.getEdad())
                + ", habito en "
                + self.getHabitat()
                + " y mi genero es "
                + self.getGenero()
            )
        else:
            nombreZona = None
            nombreZoo = None
            for zona in self.zona:
                nombreZona = zona.getNombre()
                zoo = zona.getZoo()
                nombreZoo = zoo.getNombre()
            print(
                "Mi nombre es "
                + self.getNombre()
                + ", tengo una edad de "
                + str(self.getEdad())
                + ", habito en "
                + self.getHabitat()
                + " y mi genero es "
                + self.getGenero()
                + " la zona en la que me ubico es "
                + nombreZona
                + ", en el "
                + nombreZoo
            )
            return (
                "Mi nombre es "
                + self.getNombre()
                + ", tengo una edad de "
                + str(self.getEdad())
                + ", habito en "
                + self.getHabitat()
                + " y mi genero es "
                + self.getGenero()
                + " la zona en la que me ubico es "
                + nombreZona
                + ", en el "
                + nombreZoo
            )

    def movimiento(self):
        return "desplazarse"