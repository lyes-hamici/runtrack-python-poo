from Jeu import *

carte = Carte()

carte.ajout_carte()

print(carte.get_packet_jeu_de_carte())





jeu = Jeu()

print(jeu.ajout_points_croupier())

print(jeu.ajout_points())

print(jeu.verif_gagnant())