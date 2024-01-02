class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prix_final = self.prix + self.TVA/100
        return prix_final
    

    def afficher(self):
        return f"Le produit {self.nom} coûte {self.CalculerPrixTTC()} € TVA de {self.TVA}% incluse.Hors TVA le produit coûte {self.prix}€."
    


p = Produit("pain",1.50,20)


print(p.afficher())
    



