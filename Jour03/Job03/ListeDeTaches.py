from Tache import *

class ListeDeTaches:
    def __init__(self):
        self.liste_tache = []

    def ajouterTache(self , tache):#qui permet d’ajouter une tâche.
        if tache not in self.liste_tache:
            self.liste_tache.append(tache)
    
    def supprimerTache(self,tache): #qui permet de supprimer une tâche.
        if tache in self.liste_tache:
            self.liste_tache.remove(tache)


    
    def marquerCommeFinie(self,tache): #qui permet de signaler que la tâche est faite.
        tache.statut = "terminer"
            

    
    def afficherListe(self): #qui permet de retourner une liste de toutes les tâches.
        list = []
        for i in self.liste_tache:
            list.append(i.titre + " : " + i.description + " , " + i.statut)
        return f"Voici vôtre liste de tache : {list}"
        
    
    def filterListe(self): #qui permet de filtrer les tâches par rapport à un statut et retourne cette liste.
        liste_trier = []
        for i in self.liste_tache:
            if i.statut == "à faire":
                liste_trier.append(i.titre + " : " + i.description + " , " + i.statut)
          
        return liste_trier



Liste = ListeDeTaches()

print("-------------------------")

print(Liste.afficherListe())

Liste.ajouterTache(tache)
Liste.ajouterTache(tache2)
Liste.ajouterTache(tache3)

print("-------------------------")

print(Liste.afficherListe())

print("-------------------------")

Liste.supprimerTache(tache)

print(Liste.afficherListe())

print("-------------------------")

print(Liste.filterListe())

print("-------------------------")

Liste.marquerCommeFinie(tache2)

print("-------------------------")

print(Liste.afficherListe())

print("-------------------------")

print(Liste.filterListe())
