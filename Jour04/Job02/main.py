

class Personne:
    def __init__(self,age=14):#initier à 14 de base
        self.__age = age


    def afficherAge(self):
        return self.__age
    


    def modifierAge(self,n):
        self.__age = n #nouvel age


    def bonjour(self):
        return "Hello"




class Eleve(Personne):

 
        

    def allerEnCours(self):
        return "Je vais en cours"
    



    def afficherAge(self):
        return f"J'ai {self._Personne__age} ans."
    



class Professeur(Eleve):
    def __init__(self,matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
        

    def enseigner(self):
        return f"Le cours de {self.__matiereEnseignée} va commencer."





print("TEST CLASS PERSONNE :")

parents = Personne()


print("---------------------")

print(parents.afficherAge())

print("---------------------")


parents.modifierAge(15)

print(parents.afficherAge())

parents.modifierAge(14)

print("---------------------")


parents.bonjour()

print("---------------------")
print("---------------------")





    

    

print("TEST CLASS ELEVE :")

eleve = Eleve()

print("---------------------")

print(eleve.allerEnCours())

print("---------------------")

print(eleve.afficherAge())

print("---------------------")
print("---------------------")




    


print("TEST CLASS PROFESSEUR :")

print("---------------------")

cours = Professeur("NSI")

print(cours.enseigner())



print("---------------------")
print("---------------------")



print("TEST FINAL :")

print("---------------------")

print(cours.bonjour(),cours.allerEnCours())

cours.modifierAge(15)


prof = Professeur("NSI")

prof.modifierAge(40)

print("---------------------")

print(prof.afficherAge(),prof.bonjour(),prof.enseigner())

print("---------------------")
