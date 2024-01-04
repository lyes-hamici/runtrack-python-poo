from Joueur import *
class Equipe:
    def __init__(self,nom):
        self.nom_equipe = nom
        self.list_joueur = []



    def nom_equipes(self):
        self.list_joueur.append(self.nom_equipe)



    def ajouterJoueur(self,joueur):
        if joueur not in self.list_joueur:
            self.list_joueur.append(joueur)



    def AfficherStatistiquesJoueurs(self):
        for joueur in self.list_joueur:
            print("---------------------")
            joueur.afficherStatistiques()
        print("---------------------")
        print("---------------------")
        

    def mettreAJourStatistiquesJoueur(self,prenom,but,passeD,jaune,rouge): 
         for joueur in self.list_joueur:
           if joueur.prenom == prenom:
            joueur.but = but
            joueur.passeD = passeD
            joueur.C_jaune = jaune
            joueur.C_rouge = rouge


        

akaz = Equipe("akaz")




akaz.ajouterJoueur(Leo)

akaz.ajouterJoueur(ronaldinho)

akaz.ajouterJoueur(Kevin)

akaz.AfficherStatistiquesJoueurs()

todobew = Equipe("todobew")


todobew.ajouterJoueur(Cr7)

todobew.ajouterJoueur(Neymar)

todobew.ajouterJoueur(Modric)

todobew.AfficherStatistiquesJoueurs()



todobew.mettreAJourStatistiquesJoueur("Neymar",401,37,3,2)
todobew.AfficherStatistiquesJoueurs()




Leo.marquerUnBut()

ronaldinho.marquerUnBut()

Kevin.recevoirUnCartonJaune()

Modric.effectuerUnePasseDecisive()

Cr7.marquerUnBut()

Neymar.recevoirUnCartonRouge()


akaz.AfficherStatistiquesJoueurs()
todobew.AfficherStatistiquesJoueurs()



