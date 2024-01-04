class Joueur:
    def __init__(self,prenom,nom,num,poste,but,passeD,jaune,rouge):
        self.prenom = prenom
        self.nom = nom
        self.num = num
        self.poste = poste
        self.but = but
        self.passeD = passeD
        self.C_jaune = jaune
        self.C_rouge = rouge


    def marquerUnBut(self):
        self.but += 1


    def effectuerUnePasseDecisive(self):
        self.passeD += 1


    def recevoirUnCartonJaune(self):
        self.C_jaune += 1


    def recevoirUnCartonRouge(self):
        self.C_rouge += 1

    def afficherStatistiques(self):
       print(f"Le joueur {self.prenom} {self.nom} , Numero {self.num} à marquer {self.but} buts pour {self.passeD} passe décisives.Il a reçu {self.C_jaune} carton jaunes et {self.C_rouge} carton rouge. ")
    



Leo = Joueur("Leo","Messi",9,"AD",840,350,6,4)

#print("---------------------------------------------------------------")

#print(Leo.afficherStatistiques())

Leo.recevoirUnCartonJaune()

Leo.recevoirUnCartonRouge()

Leo.marquerUnBut()

Leo.effectuerUnePasseDecisive()

#print("---------------------------------------------------------------")

#print(Leo.afficherStatistiques())


#print("---------------------------------------------------------------")


ronaldinho = Joueur("Ronaldo","de Assis Moreira",10,"AG",94 ,56,4,5)

Kevin = Joueur ("Kevin","De Bruyne",12,"MOC",64,102,5,3)

Cr7 = Joueur ("Cristiano","Ronaldo",9,"BU",870,40,5,3)

Neymar = Joueur ("Neymar","da Silva Santos",10,"AD",400,35,5,3)

Modric = Joueur ("Luka","Modric",12,"MOC",40,57,5,3)