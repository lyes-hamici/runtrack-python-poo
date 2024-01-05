from Vehicule import *

class Voiture(Vehicule):
    def __init__(self,marque, modèle, année, prix,porte=4):
        super().__init__(marque, modèle, année, prix)
        self.__porte = porte



    def set_porte(self,n):
        self.__porte = n



    def informationsVehicule(self):
        return f" Marque = {self.get_marque()} \n Modele = {self.get_modele()} \n Annee = {self.get_annee()} \n Prix = {self.get_prix()} \n Porte = {self.__porte} "
    

