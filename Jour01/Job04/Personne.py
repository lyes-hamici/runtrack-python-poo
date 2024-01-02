class Personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."
    

p = Personne("Hamici","Lyes")

print(p.SePresenter())

p = Personne("Job04","Le")

print(p.SePresenter())

    