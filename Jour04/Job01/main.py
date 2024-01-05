from Professeur import * 

class Personne:
    def __init__(self,age=14):#initier à 14 de base
        self.__age = age


    def afficherAge(self):
        return self.__age
    


    def modifierAge(self,n):
        self.__age = n #nouvel age


    def bonjour(self):
        print("Hello")


    
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



class Eleve(Personne):

 
        

    def allerEnCours(self):
        return "Je vais en cours"
    



    def afficherAge(self):
        return f"J'ai {self._Personne__age} ans."
    

    


eleve = Eleve()

print("---------------------")

print(eleve.allerEnCours())

print("---------------------")

print(eleve.afficherAge())

print("---------------------")




