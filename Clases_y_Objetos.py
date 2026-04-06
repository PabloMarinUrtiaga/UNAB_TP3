
#Crear Clase Padre
class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def hacer_sonido(self):
        return "Hace un ruido"
    
    def describir(self):
        return f"se llama {self.nombre} tiene {self.edad} años"

#Creo Clases hija con Herencia
class Perro(Animal):
    def __init__(self, nombre, edad,raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def hacer_sonido(self):
        return "Guau, Guau"
    
    def describir(self):
        return f"se lama {self.nombre} es un {self.raza} de {self.edad} años"

class Tortuga(Animal):
    def __init__(self, nombre, edad,habitat):
        super().__init__(nombre, edad)
        self.habitat = habitat
    
    def esconderse(self):
        return f"{self.nombre} se esconde en su caparazon "
    
#Instanciacion
perro=Perro("Pepe","3","Caniche")
tortuga=Tortuga("Juan","20","Agua")

#Polimorfismo
perro.hacer_sonido()
#Output: Guau, Guau

tortuga.hacer_sonido()
#Output: Hace un ruido