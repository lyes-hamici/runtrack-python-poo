class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return f"Longueur : {self.__longueur}"
    

    def set_longueur(self,n):
        self.__longueur = n



    def get_largeur(self):
        return f"Largeur : {self.__largeur}"
    

    def set_largeur(self,n):
        self.__largeur = n


r = Rectangle(5,10)

print("--------------------------")

print(r.get_largeur())

print("--------------------------")

print(r.get_longueur())

print("--------------------------")

r.set_largeur(10)

r.set_longueur(12)


print(r.get_largeur())

print("--------------------------")

print(r.get_longueur())

print("--------------------------")


