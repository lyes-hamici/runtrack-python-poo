class Carte():
    def __init__(self) -> None:
        self.carte = ["2","3","4","5","6","7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.jeu_de_carte = {}

    def ajout_carte(self):
        self.jeu_de_carte = {"Coeur" :  self.carte.copy(),

               "Trèfle" :  self.carte.copy(),

               "Carreaux":  self.carte.copy(),

               "Pique":  self.carte.copy()}
        
        

    def get_jeu_de_carte(self):
        return self.carte
    

    def get_packet_jeu_de_carte(self):
        return self.jeu_de_carte
