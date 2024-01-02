import math

class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon


    def changerRayon(self,n):
        self.rayon = n

    def circonférence(self):
        circonférence_cercle = self.rayon * math.pi
        return circonférence_cercle

    def aire(self):
        aire_cercle = self.rayon**2 * math.pi
        return aire_cercle
    
    def diametre(self):
        diametre_cercle = self.rayon / math.pi
        return diametre_cercle
    
    def afficherInfos(self):
        return f"Le cercle possede un rayon de {self.rayon} cm, un diametre de {self.diametre()} cm, une aire de {self.aire()} cm² et une circonférence de {self.circonférence()} cm."
    


c = Cercle(7)

print("-----------------")

print(c.afficherInfos())

c.changerRayon(4)

print("-----------------")

print(c.afficherInfos())

print("-----------------")