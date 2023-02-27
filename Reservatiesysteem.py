from Abu_ADT.Opdracht_3.BST import *  # import general BST
from Abu_ADT.Opdracht_3.Circular import * # import general Linked Chain
from Abu_ADT.Opdracht_2.MyQueue import * # import general Queue

print("Basic ADT's Imported")

import time

from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *

# Keuze Geadvanceerde ADT's
admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed | Thomas : ")
admin = admin.lower()

admins = ["abu","sejar","ahmed","thomas"]

while admin not in admins:
    admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed | Thomas : ")
    admin = admin.lower()

if admin == "abu":
    admin = "Abu"
    print()
    print("Searching for Abu")
    print("------",end="")
    time.sleep(0.7)
    print("------", end="")
    time.sleep(0.7)
    print("------")
    time.sleep(0.7)
    print("Hashmap Detected")
    print("------------------")
    time.sleep(0.7)
    print("Hashmap Imported")
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *


elif admin == "thomas":
    admin = "Thomas"
    print()
    print("Searching for Thomas")
    print("-------", end="")
    time.sleep(0.7)
    print("-------", end="")
    time.sleep(0.7)
    print("-------")
    time.sleep(0.7)
    print("2-3-4 Tree Detected")
    print("---------------------")
    time.sleep(0.7)
    print("2-3-4 Tree Imported")
    from Thomas_ADT.TwoTreeFourWapper import *

elif admin == "sejar":
    admin == "Sejar"
    print()
    print("Searching for Sejar")
    print("-------", end="")
    time.sleep(0.7)
    print("-------", end="")
    time.sleep(0.7)
    print("-------")
    time.sleep(0.7)
    print("Heap Detected")
    print("---------------------")
    time.sleep(0.7)
    print("Heap Imported")
    from Ahmed_ADT.heap import *

elif admin == "ahmed":
    admin == "Ahmed"
    print()
    print("Searching for Ahmed")
    print("-------", end="")
    time.sleep(0.7)
    print("-------", end="")
    time.sleep(0.7)
    print("-------")
    time.sleep(0.7)
    print("Heap Detected")
    print("---------------------")
    time.sleep(0.7)
    print("Heap Imported")
    from Ahmed_ADT.heap import *


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
