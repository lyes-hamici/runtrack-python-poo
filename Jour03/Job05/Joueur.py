from random import randint


def de(faces=6):
    """simule le lancement d'un dé
        faces: nombre de faces du dé (6 par défaut)"""
    return randint(1, faces)

class Joueur:
    """Classe du gestion d'un joueur"""
    def __init__(self, nom, image=""):
        """Création d'un joueur"""
        self.nom = nom
        self.image = image
        self._points_vie = 20  # valeur privée. la partie publique est gérée par une propriété python
        self.dexterite = 15 + de() + de()
        self.force = 15 + de() + de()
        self.experience = 0
        self.niveau = 1

    def __str__(self):
        """affichage des infos du joueur"""
        return f"Joueur: {self.nom} (pv:{self.points_vie}, xp:{self.experience}, " \
               f"nv:{self.niveau}, d:{self.dexterite}, f:{self.force})"

    def lvl_up(self):
        """passage au niveau supérieur"""
        self.niveau += 1
        self.points_vie = 20
        self.dexterite += de()
        self.force += de()
        self.experience = 0

    def choix_progression_exp(self):
        """progression du niveau avec l'expérience
           note:  progression de base proposée par M Colin"""
        # le joueur n'a pas changé du niveau
        promu = False
        # conditions pour changer de niveau
        if self.niveau == 1 and self.experience == 3:
            self.lvl_up()
            promu = True
        elif self.niveau == 2 and self.experience == 6:
            self.lvl_up()
            promu = True
        elif self.niveau == 3 and self.experience == 10:
            self.lvl_up()
            promu = True
        # le joueur a changé de niveau
        if promu:
            print(f"\o/ le joueur {self.nom} est élevé au niveau {self.niveau} ! ---")

    @property
    def points_vie(self):
        """renvoie le nombre de points de vie (propriété)"""
        return self._points_vie

    @points_vie.setter
    def points_vie(self, val):
        """fixe le nombre de points de vie - avec correction si val < 0 (setter)"""
        if val < 0:
            self._points_vie = 0
        else:
            self._points_vie = val

    def jet_attaque(self):
        """Calcule un jet d'attaque"""
        return self.force + de(20)

    def classe_armure(self):
        """calcule la classe d'armure"""
        return self.dexterite + 10