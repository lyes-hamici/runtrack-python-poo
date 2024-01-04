from random import randint


def de(faces=6):
    """simule le lancement d'un dé
        faces: nombre de faces du dé (6 par défaut)"""
    return randint(1, faces)

class Monstre:
    """gestion d'un monstre"""
    def __init__(self, categorie, difficulte, image=""):
        self.categorie = categorie
        self.difficulte = difficulte
        self.image = image
        self.points_vie = self.difficulte + de() + de()
        if categorie == "boss":
            self.dexterite = 10 + self.difficulte * 3 + de() + de()
            self.force = 10 + self.difficulte * 3 + de() + de()
            self.experience = self.difficulte * 2
        else:   # normal
            self.dexterite = 10 + self.difficulte * 2 + de()
            self.force = 10 + self.difficulte * 2 + de()
            self.experience = self.difficulte

    def __str__(self):
        """affiche les caractéristiques du monstre"""
        return f"Monstre (Axoloto:{self.categorie}, pv:{self.points_vie}, f:{self.force}, d:{self.dexterite})"

    def jet_attaque(self):
        """Calcule un jet d'attaque"""
        return self.force + de(20)

    def classe_armure(self):
        """calcule la classe d'armure"""
        return self.dexterite + 10