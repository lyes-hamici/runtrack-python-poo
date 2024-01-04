class CompteBancaire:
    def __init__(self,num,nom,prénom):
        self.__num_compte = num
        self.__nom = nom
        self.__prenom = prénom
        self.__solde = 0
        self.__decouvert = False
        self.__montant_agios = 0


    def get_name(self):
        return self.__nom
    

    def get_firstname(self):
        return self.__prenom

    def affiher(self):
        return f"Numéro de compte : {self.__num_compte} , Nom : {self.__nom} , Prénom : {self.__prenom} , Solde : {self.__solde}€"
    
    def afficherSolde(self):
        return f"Vôtre solde {self.__solde}€ ."
    
    
    def versement(self,n):
        if 0.1 <= n:
            self.__solde += n 



    def retrait(self,n):
        if 0.01 <= n <= self.__solde:
            self.__solde -= n 

        elif self.__decouvert == True and n > 0.01:
            self.__solde -= n 
            self.agios()
            self.__solde += self.__montant_agios



    def decouvert(self):
        a = input("Etes vous autoriser à etre a decovert ?: y/n ").lower()
        if a == "y":
            self.__decouvert = True

        elif a == "n":
            self.__decouvert = False

        else:
            print("Réponse invalide.")  , self.decouvert()   



    def agios(self):
        if self.__solde < 0:
            self.__montant_agios -= -(20/100 * self.__solde)
        return self.__montant_agios
    

    def get_agios(self):
        return f"Montant agios : {self.__montant_agios}€ ."
    


    def virement(self,compte,virement_banquaire):
        if type(compte) == CompteBancaire and type(virement_banquaire) == int:
            compte.versement(virement_banquaire)
            return f"Les {virement_banquaire} € du compte {self.__nom} {self.__prenom} on était transferer vers le compte de {compte.get_name()} {compte.get_firstname()}"
        else:
            return "Il n'est pas possible de faire ce virement"
                 
            







ATM = CompteBancaire(255,"Hamici","Lyes")

print("-----------------------")

print(ATM.affiher())

print("-----------------------")

ATM.versement(500)

print(ATM.afficherSolde())

print("-----------------------")

ATM.retrait(600)

print(ATM.afficherSolde())

print("-----------------------")

ATM.retrait(60)

print(ATM.afficherSolde())

print("-----------------------")

ATM.versement(-500)

print("-----------------------")

print(ATM.affiher())

print("-----------------------")


ATM.decouvert()


ATM.retrait(500)


print("-----------------------")

print(ATM.affiher())

print("-----------------------")


print(ATM.get_agios())

print("-----------------------")


ATM2 = CompteBancaire(257,"ZT","Abarax")

print(ATM.virement(ATM2,200))

print("-----------------------")

print(ATM2.affiher())

print("-----------------------")

    
        