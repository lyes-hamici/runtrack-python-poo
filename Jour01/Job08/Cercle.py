import math

class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon


    def changerRayon(self,n):
        self.rayon = n

    def circonférence(self):
        circonférence_cercle = self.rayon * math.pi
        return f"Circonférence du cercle {round(circonférence_cercle,2)}cm"

    def aire(self):
        aire_cercle = self.rayon**2 * math.pi
        return f"Aire du cercle {round(aire_cercle,2)}cm²"
    
    def diametre(self):
        diametre_cercle = self.rayon / math.pi
        return f"Diametre du cercle {round(diametre_cercle,2)}cm"
    
    def afficherInfos(self):
        return f"Le cercle possede un rayon de {self.rayon} cm, un diametre de {self.diametre()} cm, une aire de {self.aire()} cm² et une circonférence de {self.circonférence()} cm."
    


c = Cercle(7)


print(c.aire())
print("-----------------")

print(c.circonférence())
print("-----------------")

print(c.diametre())
print("-----------------")

print(c.afficherInfos())

c.changerRayon(4)

print("-----------------")

print(c.afficherInfos())

print("-----------------")