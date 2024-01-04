from random import randint
from Monstre import *
from Joueur import *


def de(faces=6):
    """simule le lancement d'un dé
        faces: nombre de faces du dé (6 par défaut)"""
    return randint(1, faces)



class Jeu:
    """Gestion du jeu et des niveaux"""
    def __init__(self, difficulte, joueur):
        """création du jeu"""
        self.difficulte = difficulte
        self.joueur = joueur
        self.niveau_etage = 1
        if self.difficulte == 1:
            self.nb_niveaux = 3
        elif self.difficulte == 2:
            self.nb_niveaux = 6
        else:  # self.difficulte == 3
            self.nb_niveaux = 10

    def combat(self, monstre):
        """gestion d'un combat"""
        print("------- COMBAT! ------")
        # Note: le premier attaquant est toujours le monstre (pourquoi pas...)
        attaquant = monstre
        defenseur = self.joueur
        # tant que les deux sont en vie
        while self.joueur.points_vie > 0 and monstre.points_vie > 0:
            print(f"### {attaquant} attaque \n    {defenseur}")
            # calcul de l'attaque
            attaque = attaquant.jet_attaque()
            print(f"jet d'attaque: {attaque}")
            # calcul de la classe d'armure
            armure = defenseur.classe_armure()
            print(f"classe d'armure: {armure}")
            # le coup a-t-il porté ?
            if attaque > armure:
                print("le coup a porté !")
                defenseur.points_vie -= attaque - armure
            # coup esquivé
            else:
                print("le coup est esquivé !")
            # on change d'attaquant et de défenseur
            if attaquant == monstre:
                attaquant = self.joueur
                defenseur = monstre
            else:
                attaquant = monstre
                defenseur = self.joueur
        # sortie de la boucle car le joueur est mort ?
        if self.joueur.points_vie <= 0:
            print("le joueur est mort...")
        # sinon le monstre est mort...
        else:
            print("le monstre est mort...")
            # progression de l'expérience du joueur
            # +2 pour un boss
            if monstre.categorie == "boss":
                self.joueur.experience += 2
            # +1 pour un monstre normal
            else:
                self.joueur.experience += 1
            # changement de niveau du joueur ?
            self.joueur.choix_progression_exp()
        print("----------------------")
        # retourne si le joueur est gagnant (toujours vivant)
        return self.joueur.points_vie > 0

    def parcourir_niveau(self):
        """Parcours d'un niveau"""
        # création des monstres
        liste_monstres = [Monstre(categorie="normal", difficulte=self.difficulte),
                          Monstre(categorie="normal", difficulte=self.difficulte),
                          Monstre(categorie="normal", difficulte=self.difficulte),
                          Monstre(categorie="normal", difficulte=self.difficulte),
                          Monstre(categorie="boss", difficulte=self.difficulte)]
        # le joueur n'a pas encore perdu
        joueur_gagnant = True
        # tant que le joueur est gagnant et qu'il reste des monstres
        while joueur_gagnant and len(liste_monstres) > 0:
            # sélectionner un monstre au hasard et le sortir de la liste
            i_monstre = randint(0, len(liste_monstres) - 1)
            monstre = liste_monstres.pop(i_monstre)
            # effectuer le combat et récupérer si le joueur est gagnant
            joueur_gagnant = self.combat(monstre)
            # si le joueur a gagné et a vaincu le boss: le niveau est fini
            if joueur_gagnant and monstre.categorie == "boss":
                return False
            # le joueur a perdu son combat
            if not joueur_gagnant:
                return True

    def parcourir_donjon(self):
        """Parcours d'un donjon en entier"""
        # tous les niveaux sont à faire
        nb_niveaux_restants = self.nb_niveaux
        # le joueur n'a pas encore perdu
        game_over = False
        # tant qu'il y a des niveaux à faire et que le joueur n'a pas perdu
        while not game_over and nb_niveaux_restants > 0:
            # parcourir le niveau et savoir si le joueur a perdu
            print(f"************* Entrée dans le niveau {self.nb_niveaux - nb_niveaux_restants + 1} *************")
            game_over = self.parcourir_niveau()
            nb_niveaux_restants -= 1
            print(f"***************************************************")
        # si le joueur n'a pas perdu : il a gagné
        if not game_over:
            print("Vous avez gagné:", self.joueur)
        # sinon il a perdu
        else:
            print("Vous avez perdu...")



# lancement du jeu
if __name__ == "__main__":
    difficulte_choisi = int(input("Choisir votre difficulté: 1= Normal, 2 = Moyen, 3 = Difficile: "))
    mon_nom = input("Donner un nom à votre personnage: ")
    mon_joueur = Joueur(nom=mon_nom)
    print(f"Bienvenue dans notre donjon, {mon_joueur.nom}")
    mon_donjon = Jeu(difficulte=difficulte_choisi, joueur=mon_joueur)
    mon_donjon.parcourir_donjon()