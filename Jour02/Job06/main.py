class Commande:
    def __init__(self):
        self.__num_commande = 0
        self.__liste_plats = []
        self.__statut = ["en cours" , "terminée" , "annulée"]
        self.__prix = []
        self.__prix_total = 0
        self.__liste_commande = {"Commande":"","Prix":"","Statut":""}
        self.__TVA = 20/100


    def ajouter_plat(self,plat,prix):
        self.__liste_plats.append(plat)
        self.liste_prix(prix)


    def get_order(self):
        return self.__liste_plats
    

    def get_prix(self):
        self.__calclule_prix()
        return self.__prix_total


    def liste_prix(self,prix):
        self.__prix.append(prix)



    def Trouver_tva(self):
        TVA = self.__prix_total + self.__TVA
        TVA = TVA - self.__prix_total
        self.__TVA = TVA


    
    def __calclule_prix(self):
        b = 0

        for i in range(len(self.__prix)):
            b += self.__prix[i]

        self.Trouver_tva()

        self.__prix_total = b + self.__TVA


    def vider_commande(self):
        self.__liste_plats = []
        self.__prix = []
        self.__liste_commande["Commande"] = self.__liste_plats
        self.__liste_commande["Prix"] = self.__prix
        self.__liste_commande["Statut"] = self.__statut[2]
        self.__num_commande += 1
        return self.__liste_commande
    

    def fin_de_commande(self):
        self.__liste_commande["Commande"] = self.__liste_plats
        self.__liste_commande["Prix"] = self.__prix
        self.__liste_commande["Statut"] = self.__statut[1]

        return self.__liste_commande , f"Prix total a payer {self.get_prix()}€ (TVA de {round(self.__TVA,2)} € incluse), Numéro de commande {self.__num_commande}"
    


    def _commande_en_cours(self):
        self.__liste_commande["Commande"] = self.__liste_plats
        self.__liste_commande["Prix"] = self.__prix
        self.__liste_commande["Statut"] = self.__statut[0]

        return self.__liste_commande ,  f"Prix total a payer {self.get_prix()}€ (TVA de {round(self.__TVA,2)} € incluse), Numéro de commande {self.__num_commande}"


    def commande_suivante(self):
        self.__liste_plats = []
        self.__prix = []
        self.__liste_commande["Commande"] = self.__liste_plats
        self.__liste_commande["Prix"] = self.__prix
        self.__liste_commande["Statut"] = ""
        self.__num_commande += 1
    



order = Commande()

order.ajouter_plat("pâte",2.50)




order.ajouter_plat("sushi",12.50)


print("-----------------------------------------------------")

print(order.fin_de_commande())

print("-----------------------------------------------------")

print(order._commande_en_cours())

print("-----------------------------------------------------")

print(order.vider_commande())

print("-----------------------------------------------------")

order.ajouter_plat("pâte",2.50)




order.ajouter_plat("sushi",12.50)


print("-----------------------------------------------------")

print(order.fin_de_commande())

print("-----------------------------------------------------")

print(order._commande_en_cours())

print("-----------------------------------------------------")


order.commande_suivante()


order.ajouter_plat("pâte",2.50)




order.ajouter_plat("sushi",12.50)


print("-----------------------------------------------------")

print(order.fin_de_commande())

print("-----------------------------------------------------")

print(order._commande_en_cours())

print("-----------------------------------------------------")

print(order.vider_commande())

print("-----------------------------------------------------")




