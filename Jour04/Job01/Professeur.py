class Professeur:
    def __init__(self,matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
        

    def enseigner(self):
        return f"Le cours de {self.__matiereEnseignée} va commencer."
    




cours = Professeur("NSI")

print(cours.enseigner())