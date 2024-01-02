class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prix_final = self.prix + self.TVA/100
        return prix_final
    

    def afficher_prix(self):
        return f"Le prix du produit est de {self.prix}€"
    

    def afficher_nom(self):
        return f"Vôtre produit ce nomme : {self.nom}."
    

    def afficher_tva(self):
        return f"La TVA est a un taux de {self.TVA}% "

    def afficher(self):
        return f"Le produit {self.nom} coûte {self.CalculerPrixTTC()} € TVA de {self.TVA}% incluse.Hors TVA le produit coûte {self.prix}€."
    
    def modif_produit(self,nom,prix,tva):
        self.nom = nom
        self.prix = prix
        self.TVA = tva
    


p = Produit("pain",1.50,20)

print("------------------------------")

print(p.afficher())
    
print("------------------------------")

p.modif_produit("pomme",2,30)


print(p.afficher())

print("------------------------------")

print("TEST INDIVIDUELLE :")

print(p.afficher_nom())

print("------------------------------")

print(p.afficher_prix())

print("------------------------------")

print(p.afficher_tva())

print("------------------------------")




