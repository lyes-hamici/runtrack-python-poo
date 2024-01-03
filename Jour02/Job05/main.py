from PIL import Image
import numpy as np

class Voiture:
    def __init__(self,marque,modèle,année,kilométrage):
        self.__marque = marque
        self.__modele = modèle
        self.__annee = année
        self.__kilometrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return f"Marque = {self.__marque}"

    def get_modele(self):
        return f"Modele = {self.__modele}"

    def get_annee(self):
        return f"Annee = {self.__annee}"

    def get_kilometrage(self):
        return f"Kilometrage = {self.__kilometrage} km"
    
    def get_en_marche(self):
        return f"Voiture en route = {self.__en_marche}"
    


    def set_marque(self,marque):
        self.__marque = marque

    def set_modele(self,modele):
        self.__modele = modele

    def set_annee(self,annee):
        self.__annee = annee

    def set_kilometrage(self,kilometrage):
        self.__kilometrage = kilometrage
    




    




    def demarrer(self):
        if  5 < self.verifier_plein() <= 50:
            self.__en_marche = True
        else:
            return "Pas assez d'essence pour demarrer."


    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir
    



v = Voiture("Skyline","GTR",1969,150_000)

print("Voiture 1")

print("-----------------")

print(v.get_modele())

print("-----------------")

print(v.get_marque())

print("-----------------")

print(v.get_annee())

print("-----------------")

print(v.get_kilometrage())

print("-----------------")

print(v.verifier_plein())

print("-----------------")

print(v.get_en_marche())

print("-----------------")

v.demarrer()

print(v.get_en_marche())

v.arreter()

print("-----------------")

print(v.get_en_marche())


print("-----------------")
print("-----------------")
print("-----------------")

v.set_marque("FERRARI")
v.set_modele("FERRARI 812 SUPERFAST")
v.set_annee(2017)
v.set_kilometrage(150_000_000_000_000_000)#Beacoup de course GTA a mon actif


print("Voiture 2")

print("-----------------")

print(v.get_modele())

print("-----------------")

print(v.get_marque())

print("-----------------")

print(v.get_annee())

print("-----------------")

print(v.get_kilometrage())

print("-----------------")

print(v.verifier_plein())

print("-----------------")

print(v.get_en_marche())

print("-----------------")

v.demarrer()

print(v.get_en_marche())

v.arreter()

print("-----------------")

print(v.get_en_marche())

print("-----------------")






