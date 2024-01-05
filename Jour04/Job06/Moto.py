from Voiture import *

class Moto(Voiture):
    def __init__(self,roue, marque, modèle, année, prix, porte=4):
        super().__init__(marque, modèle, année, prix, porte)
        self.__roue = roue


    def set_roue(self,n):
        self.__roue = n


    def demarrer(self):
        if  5 < self.verifier_plein() <= 50:
            self.__en_marche = True
            return "Vroum Vroum (bruit de moteur de fou)"
        else:
            return "Pas assez d'essence pour demarrer."


    def informationsVehicule(self):
        return f" Marque = {self.get_marque()} \n Modele = {self.get_modele()} \n Annee = {self.get_annee()} \n Prix = {self.get_prix()} \n Roue = {self.__roue} "
    






