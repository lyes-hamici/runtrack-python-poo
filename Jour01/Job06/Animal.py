class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def __str__(self) -> str: # __str__ = __repr__
        return f"L'âge de l'animal {self.age} ans."

    def vieillir(self):
        self.age += 1
        return f"L'âge de l'animal {self.age} ans."

    def nommer(self,nom):
        self.prenom = nom
        return f"L'animal se nomme {self.prenom}."

    
a = Animal()

print("-----------------")

print(a)

print("-----------------")

print(a.vieillir())

print("-----------------")

print(a.nommer("Ptit éclair"))

print("-----------------")