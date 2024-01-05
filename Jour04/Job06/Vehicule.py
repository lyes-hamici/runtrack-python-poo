class Vehicule:
    def __init__(self,marque,modèle,année,prix):
        self.__marque = marque
        self.__modele = modèle
        self.__annee = année
        self.__prix = prix
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return f"Marque = {self.__marque}"

    def get_modele(self):
        return f"Modele = {self.__modele}"

    def get_annee(self):
        return f"Annee = {self.__annee}"

    def get_prix(self):
        return f"Prix = {self.__prix} €"
    
    def get_en_marche(self):
        return f"Voiture en route = {self.__en_marche}"
    


    def set_marque(self,marque):
        self.__marque = marque

    def set_modele(self,modele):
        self.__modele = modele

    def set_annee(self,annee):
        self.__annee = annee

    def set_prix(self,prix):
        self.__prix = prix
    

    def demarrer(self):
        if  5 < self.verifier_plein() <= 50:
            self.__en_marche = True
        else:
            return "Pas assez d'essence pour demarrer."


    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir
    
    def informationsVehicule(self):
        return f" Marque = {self.__marque} \n Modele = {self.__modele} \n Annee = {self.__annee} \n Prix = {self.__prix} "
    



    