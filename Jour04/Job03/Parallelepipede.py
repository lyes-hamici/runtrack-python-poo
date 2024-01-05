from Rectangle import *

class Parallelepipede(Rectangle):
    def __init__(self,hauteur,longueur,largeur):
        super().__init__(longueur,largeur)
        self.__hauteur = hauteur


    def get_hauteur(self):
        return f"Hauteur : {self.__hauteur} cm"
    

    def set_hauteur(self,n):
        self.__hauteur = n 


    
    def volume(self):
        vol = self.surface() * self.__hauteur
        return f"Volume {vol}"
    

    
    






