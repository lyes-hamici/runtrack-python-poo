class Ville:
    def __init__(self):
        self.__nom = "" 
        self.__nbr_habitants = 0


    def __str__(self) -> str:
        return f"Population de la vile de  {self.__nom} : {self.__nbr_habitants} habitants"


    def get_ville(self):
        return self.__nom
    

    def get_nbr_habitants(self):
        return self.__nbr_habitants
    


    def set_ville(self,ville):
         self.__nom = ville
    

    def set_nbr_habitants(self,n):
        self.__nbr_habitants += n

    
    def ajouterPopulation_Ville(self):
        self.__nbr_habitants += 1




v = Ville()

v.set_ville("Paris")

v.set_nbr_habitants(1_000_000)



#print(v.get_ville())



#print(v.get_nbr_habitants())



#print(v)





v2 = Ville()


v2.set_ville("Marseille")

v2.set_nbr_habitants(861_635)

#print(v2)


#print(v2.get_ville())


#print(v2.get_nbr_habitants())



#print(v2)







