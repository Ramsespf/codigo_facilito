class Animal:    # Clase Padre
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')

class Mascota(Animal): 
    
    def comer(self):        # Sobreescribir metodo, solo basta con volver a definir dicho metodo
        print('La mascota come')

    

class Felino:

    def cazar(self):
        print('El felino caza')
        

class Gato(Mascota, Felino):    # Clase Hija, Herencia multiple

    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def comer(self):
        super().comer()         # Esta funcion nos permite acceder al metodocomer de la clase padre inmediata superior
        print(f'{self.nombre} come.')

    def dormir(self):
        print(f'{self.nombre} duerme.')

docky = Gato('Docky')

docky.comer()
docky.dormir()
docky.cazar()