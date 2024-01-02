class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon


    def changerRayon(self,n):
        self.rayon = n

    def circonférence(self):
        circonférence_cercle = self.rayon * 3.14
        return circonférence_cercle

    def aire(self):
        aire_cercle = self.rayon**2 * 3.14
        return aire_cercle
    
    def diametre(self):
        diametre_cercle = self.rayon / 3.14
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