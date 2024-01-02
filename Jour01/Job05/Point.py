class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Les coordonnées du point sont x = {self.x} et y = {self.y}."
    
    def afficherY(self):
        return f"Coordonnées de y = {self.y}"
    
    def afficherX(self):
        return f"Coordonnées de x = {self.x}"
    
    def changerX(self,n):
        self.x = n

    def changerY(self,n):
        self.y = n


p = Point(5,8)


print("-----------------")
print(p.afficherLesPoints())
print("-----------------")
print(p.afficherX())
print("-----------------")
print(p.afficherY())
print("-----------------")

p.changerX(4)
p.changerY(12)

print(p.afficherLesPoints())
print("-----------------")