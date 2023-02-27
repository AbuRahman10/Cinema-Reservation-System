from Abu_ADT.Opdracht_3.BST import *
from Abu_ADT.Opdracht_3.Circular import *
from Abu_ADT.Opdracht_2.MyQueue import *
from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *

# Keuze Geadvanceerde ADT's
admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed | Thomas : ")
admin = admin.lower()

if admin == "abu":
    admin = "Abu"
    print("--------------")
    yes_no = input("Hashmap Available, Import? (yes/no): ")
    yes_no = yes_no.lower()
    if yes_no == "yes":
        from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
        print("-----------------")
        print("Hashmap Imported")



elif admin == "thomas":
    admin = "Thomas"

elif admin == "sejar":
    admin = "Sejar"

elif admin == "ahmed":
    admin = "Ahmed"


class Reservatiesysteem:

    def __init__(self):
        """
        Hier worden alle kettingen en bomen aangemaakt
        mijn voorkeur gaat naar alles apart in een ketting zetten voor simpele beereikbaarheid
        en gebruikers in een boom voor sneller te zoeken.
        """
        #self.zaal = LinkedChain()
        #self.film = LinkedChain()
        #self.gebruiker = BST()
        #self.reservatie = LinkedChain()
        #self.vertoning = LinkedChain()
