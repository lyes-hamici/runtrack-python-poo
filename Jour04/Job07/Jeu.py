from Carte import *
import random

class Jeu(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.points = 0
        self.points_final = 0
        self.points_croupier = 0
        self.points_final_croupier = 0


    def ajout_points(self):

        print("--------------------------------")

        if self.points_final >= 22:
                print("--------------------------------")
                print(f"Vous avez sauter score {self.points_final}")
                print("--------------------------------")
                return self.verif_gagnant()

        elif self.points_final == 21:
                print("--------------------------------")
                print(f"Blackjack : {self.points_final}")
                print("--------------------------------")
                return self.verif_gagnant()

        val = random.choice(self.carte)

        print("Val : ",val)
        if val == "2":
            self.points = 2
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)
            
        elif val == "3":
            self.points = 3
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)

        elif val == "4":
            self.points = 4
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)

        elif val == "5":
            self.points = 5
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)

        elif val == "6":
            self.points = 6
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)
            

        elif val == "7":
            self.points = 7
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "8":
            self.points = 8
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "9":
            self.points = 9
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "10":
            self.points = 10
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "Roi":
            self.points = 10
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "Dame":
            self.points = 10
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "Valet":
            self.points = 10
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "As" and self.points_final < 11:
            self.points = 11
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)


        elif val == "As" and self.points_final >= 11:
            self.points = 1
            self.points_final += self.points
            print("Nouveau point : ",self.points_final)

        if self.points_final >= 21:
                print(f"Vous avez sauter score {self.points_final}")
                return self.verif_gagnant()
        

        elif self.points_final == 21:
                print(f"Blackjack : {self.points_final}")
                return self.verif_gagnant()
        

        repeat = input("Voulez vous repiocher ? y/n : ")
        if repeat == "y":
            if self.points_final >= 22:
                print("--------------------------------")
                print(f"Vous avez sauter score {self.points_final}")
                print("--------------------------------")
                return self.verif_gagnant()

            elif self.points_final == 21:
                print("--------------------------------")
                print(f"Blackjack : {self.points_final}")
                print("--------------------------------")
                return self.verif_gagnant()
                
            else:
                self.ajout_points()

        

        elif repeat == "n":
           print("--------------------------------")
           print(f"Votre score : {self.points_final}")
           print("--------------------------------")
           
        else:
            print("Choix incoreect.")
            exit()




    def ajout_points_croupier(self):

        while self.points_final_croupier < 17 :

            print("--------------------------------")

            if self.points_final_croupier == 21:
                    print("--------------------------------")
                    print(f"Blackjack : {self.points_final_croupier}")
                    print("--------------------------------")
                    return self.verif_gagnant()
            
            elif self.points_final_croupier > 21:
                    print("--------------------------------")
                    print(f"Le croupier à sauter : {self.points_final_croupier}")
                    print("--------------------------------")
                    return self.verif_gagnant()

            val = random.choice(self.carte)

            print("Val : ",val)
            if val == "2":
                self.points_croupier_croupier = 2
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)
                
            elif val == "3":
                self.points_croupier = 3
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)

            elif val == "4":
                self.points_croupier = 4
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)

            elif val == "5":
                self.points_croupier = 5
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)

            elif val == "6":
                self.points_croupier = 6
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)
                

            elif val == "7":
                self.points_croupier = 7
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "8":
                self.points_croupier = 8
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "9":
                self.points_croupier = 9
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "10":
                self.points_croupier = 10
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "Roi":
                self.points_croupier = 10
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "Dame":
                self.points_croupier = 10
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "Valet":
                self.points_croupier = 10
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "As" and self.points_final_croupier < 11:
                self.points_croupier = 11
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)


            elif val == "As" and self.points_final_croupier >= 11:
                self.points_croupier = 1
                self.points_final_croupier += self.points_croupier
                print("Point croupier : ",self.points_final_croupier)

            
            
            if self.points_final_croupier > 21:
                print("--------------------------------")
                print(f"Le croupier à sauter score {self.points_final_croupier}")
                print("--------------------------------")
                return self.verif_gagnant()
                

            elif self.points_final_croupier == 21:
                    print("--------------------------------")
                    print(f"Blackjack : {self.points_final_croupier}")
                    print("--------------------------------")
                    return self.verif_gagnant()
            
        print("--------------------------------")
            
            




    def verif_gagnant(self):
            if self.points_final > self.points_final_croupier and self.points_final < 22 and self.points_final_croupier < 22:
                print(f"Joueur gagnant avec {self.points_final} points")
                exit()
            
            elif self.points_final < self.points_final_croupier and self.points_final < 22 and self.points_final_croupier < 22:
                print(f"Croupier gagnant avec {self.points_final_croupier} points")
                exit()
            
            elif self.points_final_croupier > 21:
                print(f"Joueur gagnant avec {self.points_final} points")
                exit()
            
            elif self.points_final > 21:
                print(f"Croupier gagnant avec {self.points_final_croupier} points")
                exit()
