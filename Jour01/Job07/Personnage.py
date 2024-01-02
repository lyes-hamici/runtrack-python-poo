class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 0

    #V2
    '''def __init__(self,x,y):
        self.x = 0
        self.y = 0'''


        

    def bas(self):
        self.y = self.y - 1

    def haut(self):
        self.y = self.y + 1

    def droite(self):
        self.x = self.x + 1

    def gauche(self):
        self.x = self.x - 1

    def position(self):
        t = (self.x,self.y)
        return f"Les coordonnées du personage sont {t}."
    

        

#p = Personnage(5,5) pour la V2

p = Personnage()

print("-----------------")

print(p.position())

print("-----------------")

p.gauche()
print("Aller a gauche",p.position())

print("-----------------")

p.droite()
print("Aller a droite",p.position())

print("-----------------")

p.haut()
print("Aller en haut",p.position())

print("-----------------")

p.bas()
print("Aller en bas",p.position())

print("-----------------")