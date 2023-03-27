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
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
    from Abu_ADT.Opdracht_3.BSTtable import *
    from Abu_ADT.Opdracht_4.Hashmap.HashmapTable import *  # import general Linked Chain
    from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue

elif admin == "thomas":
    admin = "Thomas"
    from Thomas_ADT.TwoTreeFourWapper import *
    from Abu_ADT.Opdracht_3.BSTtable import *
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
    from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue

elif admin == "sejar":
    admin = "Sejar"
    from Sejar_ADT.Heap import *
    from Abu_ADT.Opdracht_3.BSTtable import *
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
    from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue


elif admin == "ahmed":
    admin = "Ahmed"
    from Ahmed_ADT.heap import *
    from Abu_ADT.Opdracht_3.BSTtable import *
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
    from Abu_ADT.Opdracht_2.MyQueue import *  # import general Queue

class Reservatiesysteem:

    def __init__(self):
        """
        Hier worden alle kettingen en bomen aangemaakt
        mijn voorkeur gaat naar alles apart in een ketting zetten voor simpele beereikbaarheid
        en gebruikers in een boom voor sneller te zoeken.
        """
        self.zalen = LinkedChainTable()

        self.films = LinkedChainTable()

        self.gebruikers = BSTTable()
        #self.gebruikers = TwoThreeFourTreeTable()

        self.reservaties = LinkedChainTable()

        self.vertoningen = LinkedChainTable()

    def addGebruiker(self, id, voornaam, achternaam, emailadres):

        gebruiker = Gebruiker()
        if self.gebruikers.tableRetrieve(id)[1]:
            print(str(emailadres + " bestaat al!"))
            return False

        gebruiker.maak_gebruiker(id, voornaam, achternaam, emailadres)
        self.gebruikers.tableInsert((id, gebruiker)) # hier moeten we de object zelf inserten ipv input

        print("Gebruiker met id " + str(id) + " is gemaakt!")
        return True

    def addFilm(self, id, titel, rating):

        film = Film()
        if self.films.tableRetrieve(id)[1]:
            print(titel + " bestaat al!")
            return False

        film.voegfilmtoe(id, titel, rating)
        self.films.tableInsert(id, film)

        print(titel + " is gemaakt!")
        return True

    def addReservatie(self, id, userid, timestamp, vertoningid, aantalplaatsen):
        reservatie = Reservatie()
        if self.reservaties.tableRetrieve(id)[1]:
            print("Reservatie van " + userid + " Bestaat al")
            return False

        reservatie.maak_reservatie(id, userid, timestamp, vertoningid, aantalplaatsen)
        self.reservaties.tableInsert(id, reservatie)
        print("Reservatie van " + str(userid) + " is aangemaakt!")
        return True

    def addVertoning(self,id,zaalnummer,slot,datum,filmid):
        vertoning = Vertoning()
        if self.vertoningen.tableRetrieve(id)[1]:
            print("Vertoning met id", id, "bestaat al")
            return False

        vertoning.maak_vertoning(id,zaalnummer,slot,datum,filmid)
        self.vertoningen.tableInsert(id,vertoning)
        print("Film met " + str(filmid) + " id is aangemaakt!")
        return True

    def addZaal(self,zaalnummer,plaatsen):
        zaal = Zaal()
        if self.zalen.tableRetrieve(id)[1]:
            print(str(zaalnummer) + " Bestaat al")
            return False

        zaal.maak_zaal(zaalnummer,plaatsen)
        self.vertoningen.tableInsert(zaalnummer, zaal)
        print("zaal " + str(zaalnummer) + " is aangemaakt!")
        return True

    def getVertoning(self,id):
        return self.vertoningen.tableRetrieve(id)[1]

