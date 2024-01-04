from Ville import *


class Personne:

    def __init__(self):
        self.__nom = ""
        self.__age = ""
        self.ville = Ville()#rappel de ma class Ville


    def ajouterPersonne(self,nom,age,ville):
        self.__nom = nom 
        self.__age = age
        self.ajouterPopulation(ville)#renvoi du nom de ma ville à ajouterPopulation() pour verifier ça ville et ajouter un habitant
        return f"Bienvenue {self.__nom} , {self.__age} ans , habitant à {ville}"


    def ajouterPopulation(self,ville):
        if ville == "Paris":
            v.ajouterPopulation_Ville()#appel a v ma premiere ville cree dans ma class Ville ainsi que de la fonction qui va mettre à jour mes attribu dans ma class Ville.

        elif ville == "Marseille":
            v2.ajouterPopulation_Ville()#appel a v2 ma deuxieme ville cree dans ma class Ville ainsi que de la fonction qui va mettre à jour mes attribu dans ma class Ville.








p = Personne()

print("--------------------------------")

print("Population avant ajout :")

print(v2)
print(v)

print("--------------------------------")
print("--------------------------------")
print("--------------------------------")

print("Ajout Population :")

print(p.ajouterPersonne("John",45,"Paris"))
print("--------------------------------")
print(p.ajouterPersonne("Myrtille,",4,"Paris"))
print("--------------------------------")
print(p.ajouterPersonne("18",45,"Marseille"))

print("--------------------------------")
print("--------------------------------")
print("--------------------------------")


print("Population apres ajout :")

print(v2)
print(v)

print("--------------------------------")


