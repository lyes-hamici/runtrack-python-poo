from Rectangle import *
from Parallelepipede import *



rect = Rectangle(10,5)

print("--------------------------------------------------------------------------------------------------------------------------------------------")

print(rect.get_largeur(),rect.get_longueur())

print("--------------------------------------------------------------------------------------------------------------------------------------------")

rect.set_largeur(15),rect.set_longueur(10)

print(rect.get_largeur(),rect.get_longueur())

print("--------------------------------------------------------------------------------------------------------------------------------------------")


para = Parallelepipede(5,5,15)


print(para.volume())

print("--------------------------------------------------------------------------------------------------------------------------------------------")