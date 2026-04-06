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
    
    def opuestos(self):
        return -self.x, -self.y
    
Punto1 = Punto(3,5)

#Impresion del Eje x
print(Punto1.eje_x())

#Impresion del Eje Y
print(Punto1.eje_y())

#Impresion del ambos ejes en un Str
print(Punto1.impresion())

#Impresion del opuesto de nuestro punto:
print(Punto1.opuestos())