#Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
# constructor que recibe ambos valores.
# ● Definir métodos tales como:
# ○ eje_x
# ○ eje_y
# ○ impresion (método que devuelve en representación de string ambos valores)
# ○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
# negativos-)
# ○ Cualquier otro método que considere importante

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y
    
    def impresion(self):
        return f"el punto esta en X: {self.x} e Y: {self.y}"
    
    def opuesto(self):
        return Punto(-self.x, -self.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    
Punto1 = Punto(3,5)
Punto2 = Punto (7,7)

#Impresion del Eje x
#print(Punto1.eje_x())

#Impresion del Eje Y
#print(Punto1.eje_y())

#Impresion del ambos ejes en un Str
#print(Punto1.impresion())

#Impresion del opuesto de nuestro punto:
print(Punto1.opuesto())

#Ejercicio 3:
# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.

# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

class Linea():
    def __init__(self,Punto1: Punto, Punto2:Punto):
        self.Punto1 = Punto1
        self.Punto2 = Punto2

    def mueve_derecha(self,numero: int):
        self.Punto1.x += numero
        self.Punto2.x += numero
        return f"{self.Punto1.eje_x()},{self.Punto1.eje_y()} y , {self.Punto2.eje_x()},{self.Punto2.eje_y()}"
    
    def mueve_izquierda(self,numero: int):
        self.Punto1.x -= numero
        self.Punto2.x -= numero
        return f"{self.Punto1.eje_x()};{self.Punto1.eje_y()}  , {self.Punto2.eje_x()};{self.Punto2.eje_y()}"
    
    def mueve_arriba(self,numero: int):
        self.Punto1.y += numero
        self.Punto2.y += numero
        return f"{self.Punto1.eje_x()};{self.Punto1.eje_y()}  , {self.Punto2.eje_x()};{self.Punto2.eje_y()}"
    
    def mueve_abajo(self,numero: int):
        self.Punto1.y -= numero
        self.Punto2.y -= numero
        return f"{self.Punto1.eje_x()};{self.Punto1.eje_y()}  , {self.Punto2.eje_x()};{self.Punto2.eje_y()}"
    
        
        
#p1 (3,5)
#p2 (7,7)

Linea1 = Linea(Punto1,Punto2)

#print(Linea1.mueve_abajo(2))

# Ejercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.

# Con los siguientes métodos:

# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción

class Cancion():
    def __init__(self,titulo: str,autor:str):
        self.titulo = titulo
        self.autor = autor
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self,nombre_nuevo:str):
        self.titulo = nombre_nuevo
        return self.titulo
    
    def set_autor(self,nombre_nuevo:str):
        self.autor = nombre_nuevo
        return self.autor
    
Cancion1= Cancion("Fantasia y Realidad","Callejeros")

# Ejercicio 5:
# ● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
# servicios: getters y setters, método para leer la información y método para mostrar la
# información.
# ● Este último método mostrará la información del libro con este formato:
#     Título: Introduction to Java Programming 3a. edición
#     Autor: Liang, Y. Daniel
#     ISBN: 0-13-031997-X
#     Prentice-Hall, New Jersey (USA)
#     viernes 16 de noviembre de 2001
#     784 páginas

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
        
class Libro():
    def __init__(self, titulo:str, autor:Persona, ISBN:str, paginas:int, edicion:str, editorial:str, lugar:str, fecha_de_emision:str):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_de_emision = fecha_de_emision
        
    def mostrar_datos(self):
        return f"""
     Título: {self.titulo} , {self.edicion} edicion
     Autor: {self.autor}
     ISBN: {self.ISBN}
     {self.editorial}, {self.lugar}
     {self.fecha_de_emision}
     {self.paginas} páginas
     """

Autor1 = Persona("Pablo","Marin",18)

Libro1 = Libro("Luna de pluton",Autor1,"0-13-031997-X",100,"1era","Viva la vida", "Burzaco", "Hoy :D")

print(Libro1.mostrar_datos())
    
        
        
