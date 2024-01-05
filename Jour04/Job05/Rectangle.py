from Forme import * 

class Rectangle(Forme):
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur



    def get_longueur(self):
        return f"Longueur : {self.__longueur} cm"
    

    def get_largeur(self):
        return f"Largeur : {self.__largeur} cm"
    

    def set_longueur(self,n):
        self.__longueur = n 


    def set_largeur(self,n):
        self.__largeur = n 

    def perimètre(self):
        peri = 2*(self.__longueur + self.__largeur)
        return f"Le perimètre est de {peri} cm."
    

    def surface(self):
        surface_rectangle = self.__largeur * self.__longueur
        return f"La surface est de {surface_rectangle} cm."
    

    def aire(self):
        aire_rect = self.__largeur * self.__longueur
        return f"L'aire du rectangle de longueur : {self.__longueur} cm et de largeur : {self.__largeur} cm vaut {aire_rect} cm²" 


