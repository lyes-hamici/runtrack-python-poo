from Vehicule import *

class Voiture(Vehicule):
    def __init__(self,marque, modèle, année, prix,porte=4):
        super().__init__(marque, modèle, année, prix)
        self.__porte = porte



    def set_porte(self,n):
        self.__porte = n

    def demarrer(self):
        if  5 < self.verifier_plein() <= 50:
            self.__en_marche = True
            return f"Avec {self.get_modele()} {self.get_marque()} vous êtes satellisé."
        else:
            return "Pas assez d'essence pour demarrer."




    def informationsVehicule(self):
        return f" Marque = {self.get_marque()} \n Modele = {self.get_modele()} \n Annee = {self.get_annee()} \n Prix = {self.get_prix()} \n Porte = {self.__porte} "
    

