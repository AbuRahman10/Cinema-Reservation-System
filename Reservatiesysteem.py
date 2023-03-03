import time

from Abu_ADT.Opdracht_3.BST import *  # import general BST
from Abu_ADT.Opdracht_3.Circular import *  # import general Linked Chain
from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue

from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *


# Keuze Geadvanceerde ADT's
# admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed | Thomas : ")
# admin = admin.lower()

# admins = ["abu","sejar","ahmed","thomas"]


# while admin not in admins:
#     admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed | Thomas : ")
#     admin = admin.lower()
#
# if admin == "abu":
#     admin = "Abu"
#     print()
#     print("Searching for " + admin)
#     print("------",end="")
#     time.sleep(0.7)
#     print("------", end="")
#     time.sleep(0.7)
#     print("------")
#     time.sleep(0.7)
#     from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
#     from Abu_ADT.Opdracht_3.BST import *  # import general BST
#     from Abu_ADT.Opdracht_3.Circular import *  # import general Linked Chain
#     from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue
#     print("Hashmap Detected")
#     print("------------------")
#     time.sleep(0.7)
#     print("Hashmap Imported")
#
#
#
# elif admin == "thomas":
#     admin = "Thomas"
#     print()
#     print("Searching for " + admin)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------")
#     time.sleep(0.7)
#     from Thomas_ADT.TwoTreeFourWapper import *
#     from Abu_ADT.Opdracht_3.BST import *  # import general BST
#     from Abu_ADT.Opdracht_3.Circular import *  # import general Linked Chain
#     from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue
#     print("2-3-4 Tree Detected")
#     print("---------------------")
#     time.sleep(0.7)
#     print("2-3-4 Tree Imported")
#
#
# elif admin == "sejar":
#     admin = "Sejar"
#     print()
#     print("Searching for " + admin)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------")
#     time.sleep(0.7)
#     from Sejar_ADT.Heap import *
#     from Abu_ADT.Opdracht_3.BST import *  # import general BST
#     from Abu_ADT.Opdracht_3.Circular import *  # import general Linked Chain
#     from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue
#     print("Heap Detected")
#     print("---------------------")
#     time.sleep(0.7)
#     print("Heap Imported")
#
#
# elif admin == "ahmed":
#     admin = "Ahmed"
#     print()
#     print("Searching for " + admin)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------", end="")
#     time.sleep(0.7)
#     print("-------")
#     time.sleep(0.7)
#     from Ahmed_ADT.heap import *
#     from Abu_ADT.Opdracht_3.BST import *  # import general BST
#     from Abu_ADT.Opdracht_3.Circular import *  # import general Linked Chain
#     from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue
#     print("Heap Detected")
#     print("---------------------")
#     time.sleep(0.7)
#     print("Heap Imported")


class Reservatiesysteem:

    def __init__(self):
        """
        Hier worden alle kettingen en bomen aangemaakt
        mijn voorkeur gaat naar alles apart in een ketting zetten voor simpele beereikbaarheid
        en gebruikers in een boom voor sneller te zoeken.
        """
        self.zalen = LinkedChain()
        self.films = LinkedChain()
        self.gebruikers = BST()
        self.reservaties = LinkedChain()
        self.vertoningen = LinkedChain()

    def addGebruiker(self, id, voornaam, achternaam, emailadres):

        gebruiker = Gebruiker()
        if self.gebruikers.searchTreeRetrieve(id)[1]:
            print(gebruiker.zoek_gebruiker(id) + " bestaat al!")
            return False

        input = gebruiker.maak_gebruiker(id, voornaam, achternaam, emailadres)
        self.gebruikers.searchTreeInsert((id,input))

        print(gebruiker.zoek_gebruiker(id) + " is gemaakt!")
        return True




