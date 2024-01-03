class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
        

    def get_titre(self):
        return f"Titre du livre : {self.__titre}"
    

    def get_auteur(self):
        return f"Auteur du livre : {self.__auteur}"
    

    def get_page(self):
        return f"Nombre de page du livre : {self.__pages}"
    

    def set_titre(self,titre):
        self.__titre = titre

    
    def set_auteur(self,auteur):
        self.__auteur = auteur


    def set_page(self,page):
        if page > 0 and isinstance(page, int):
            self.__pages = int(page)

        else:
            print("-------------------------")
            print ("Ce nombre de page n'est pas un nombre entier/positif , le nombre de page n'est donc pas modifier.")
            print("-------------------------")



    def verification(self):
        if self.__disponible == True:
            return  True
        else:
            return False
        

    def emprunter(self):
        
        if self.verification() == True:
            self.__disponible = False
            return "Vous avez emprunter ce livre."

        else:
            return "Livre déja emprunter."
        

    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
            return "Livre rendu."
        
        else:
            return "Ce livre est déja ici."



livre = Livre("Dragon Ball, tome 1 : Sangoku","Akira Toriyama",187)

print("-------------------------")

print(livre.get_titre())

print("-------------------------")

print(livre.get_auteur())

print("-------------------------")

print(livre.get_page())

print("-------------------------")
print("-------------------------")

livre.set_titre("Pokémon, La Grande Aventure - tome 1")

livre.set_auteur("Hidenori Kusaka")

livre.set_page(512.6)




print("Changement des valeurs :")

print("-------------------------")
print("-------------------------")

print(livre.get_titre())

print("-------------------------")

print(livre.get_auteur())

print("-------------------------")

print(livre.get_page())

print("-------------------------")

livre.set_page(512)

print(livre.get_page())

print("-------------------------")



print(livre.verification())

print("-------------------------")

print(livre.emprunter())

print("-------------------------")

print(livre.verification())

print("-------------------------")

print(livre.emprunter())

print("-------------------------")


print(livre.rendre())

print("-------------------------")

print(livre.rendre())

print("-------------------------")



