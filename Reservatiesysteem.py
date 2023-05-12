import base64
import datetime
from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *
from Clock import timer
import pandas as pd

admin = input("Choice Admins - Abu | Sejar | Ahmed : ")
admin = admin.lower()
admins = ["abu","sejar","ahmed"]
while admin not in admins:
    admin = input("Choice Admins - Abu | Sejar | Ahmed : ")
    admin = admin.lower()
if admin == "abu":
    admin = "Abu"
elif admin == "sejar":
    admin = "Sejar"
elif admin == "ahmed":
    admin = "Ahmed"

# KEUZE GEAVANCEERDE ADT'S
bst = input("Choice BST - Abu | Sejar | Ahmed : ")
bst = bst.lower()
while bst not in admins:
    bst = input("Choice BST - Abu | Sejar | Ahmed : ")
    bst = bst.lower()
if bst == "abu":
    from Abu_ADT.Opdracht_3.BSTtable import *
elif bst == "sejar":
    from Sejar_ADT.BSTWrapper import *
elif bst == "ahmed":
    from Ahmed_ADT.BSTWrapper import *

linkedchain = input("Choice LinkedChain - Abu | Sejar | Ahmed : ")
linkedchain = linkedchain.lower()
while linkedchain not in admins:
    linkedchain = input("Choice LinkedChain - Abu | Sejar | Ahmed : ")
    linkedchain = linkedchain.lower()
if linkedchain == "abu":
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
elif linkedchain == "sejar":
    from Sejar_ADT.LinkedChainTable import *
elif linkedchain == "ahmed":
    from Ahmed_ADT.LinkedChainTable import *

heaps = ["sejar","ahmed"]
heap = input("Choice Heap - Sejar | Ahmed : ")
heap = heap.lower()
while heap not in heaps:
    heap = input("Choice Heap - Sejar | Ahmed : ")
    heap = heap.lower()
if heap == "sejar":
    from Sejar_ADT.heapWrapper import *
elif heap == "ahmed":
    from Ahmed_ADT.heapWrapper import *

queue = input("Choice Queue - Abu | Sejar | Ahmed : ")
queue = queue.lower()
while queue not in admins:
    queue = input("Choice Queue - Abu | Sejar | Ahmed : ")
    queue = queue.lower()
if queue == "sejar":
    from Sejar_ADT.queueTable import *
elif queue == "ahmed":
    from Ahmed_ADT.queueTable import *
elif queue == "abu":
    from Abu_ADT.Opdracht_2.queueTable import *

queue_heaps = ["queue","heap"]
queue_heap = input("Reservatie Klasse: Queue of Heap?: ")
queue_heap = queue_heap.lower()
while queue_heap not in queue_heaps:
    queue_heap = input("Reservatie Klasse: Queue of Heap?: ")
    queue_heap = queue_heap.lower()

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
        if queue_heap == "queue":
            self.reservaties = heapTable()
        elif queue_heap == "heap":
            self.reservaties = queueTable()
        self.vertoningen = LinkedChainTable()

        # alleen bij LINKEDCHAIN!
        self.indexVertoning = 1
        self.indexFilm = 1
        self.indexZaal = 1

    def getVertoningen(self):
        return self.vertoningen.save()
    def getFilms(self):
        return self.films.save()
    def getGebruikers(self):
        return self.gebruikers.save()
    def getReservaties(self):
        return self.reservaties.save()
    def getZalen(self):
        return self.zalen.save()
    def getVertoning(self,id):
        vertoningen = self.getVertoningen()
        vertoning = Vertoning()
        bestaat = False
        for i in vertoningen:
            if i.id == id:
                vertoning = i
                bestaat = True
        return vertoning,bestaat
    def getZaal(self,zaalnummer):
        zaal = Zaal()
        zaal_bestaat = False
        zalen = self.getZalen()
        for zl in zalen:
            if zl.nummer == zaalnummer:
                zaal_bestaat = True
                zaal = zl
        return zaal,zaal_bestaat

    def getGebruiker(self,id):
        return self.gebruikers.tableRetrieve(id)
    def addGebruiker(self, id, voornaam, achternaam, emailadres):
        gebruiker = Gebruiker()
        if self.gebruikers.tableRetrieve(id)[1]:
            print("\033[1;31mGebruiker met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
            return False
        gebruiker.maak_gebruiker(id, voornaam, achternaam, emailadres)
        self.gebruikers.tableInsert((id, gebruiker))
        print("Gebruiker met id " + str(id) + " is gemaakt!")
        return True
    def addFilm(self, id, titel, rating):
        film = Film()
        for i in self.getFilms():
            if i.id == id or i.get_titel() == titel:
                print("\033[1;31mFilm met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
                return False
        film.voegfilmtoe(id, titel, rating)
        if (self.films.tableInsert(self.indexFilm, film)):
            self.indexFilm += 1
            print(titel + " is aangemaakt!")
        return True
    def addVertoning(self,id,zaalnummer,slot,datum,filmid, vrijePlaatsen):
        vertoning = Vertoning()
        for i in self.getVertoningen():
            if i.id == id or (i.datum == datum and i.slot == slot and i.get_zaalnummer() == zaalnummer):
                print("\033[1;31mVertoning met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
                return False
        zaal, zaal_bestaat = self.getZaal(zaalnummer)
        if zaal_bestaat is False:
            print("\033[1;31mZaal met nummer: \033[0m" + str(zaalnummer) + " \033[1;31mbestaat niet!\033[0m")
            return False
        vertoning.maak_vertoning(id,zaalnummer,slot,datum,filmid, vrijePlaatsen)
        if (self.vertoningen.tableInsert(self.indexVertoning,vertoning)):
            print("Vertoning " + str(id) + " is aangemaakt!")
            self.indexVertoning += 1
        return True
    def addZaal(self,zaalnummer,plaatsen):
        zaal = Zaal()
        for i in self.getZalen():
            if i.nummer == zaalnummer:
                print("\033[1;31mZaal met id: \033[0m" + str(zaalnummer) + " \033[1;31mis al gemaakt!\033[0m")
                return False
        zaal.maak_zaal(zaalnummer,plaatsen)
        if (self.zalen.tableInsert(self.indexZaal, zaal)):
            print("Zaal " + str(zaalnummer) + " is aangemaakt!")
            self.indexZaal += 1
        return True
    def addReservatie(self, timestamp, userid, vertoningid, tickets):
        reservatie = Reservatie()
        vertoning, bestaat = self.getVertoning(vertoningid)
        gebruiker_bestaat = self.getGebruiker(userid)[1]
        if bestaat is False or gebruiker_bestaat is False or tickets >= vertoning.get_vrije_plaatsen():
            print("\033[1;31mReservatie van user: \033[0m" + str(userid) + " \033[1;31mkan niet aangemaakt worden!\033[0m")
            return False
        aantal_vrij = vertoning.get_vrije_plaatsen() - tickets  # AANPASSING VRIJE PLAATSEN
        vertoning.vrijeplaatsen = aantal_vrij
        vertoning.reservaties += tickets
        reservatie.maak_reservatie(timestamp, userid, vertoningid, tickets)
        if self.reservaties.tableInsert((userid,reservatie)):
            print("Reservatie van user " + str(userid) + " is aangemaakt!")
        return True
    def updateTickets(self, vertoning_id, tickets):
        vertoning, vertoning_bestaat = self.getVertoning(vertoning_id)
        if vertoning_bestaat:
            vertoning.plaatsenbezet += tickets
            if vertoning.plaatsenbezet <= vertoning.reservaties:
                zaal, zaal_bestaat = self.getZaal(vertoning.get_zaalnummer())
                if zaal_bestaat and vertoning.get_plaatsenbezet() + vertoning.get_vrije_plaatsen() == zaal.get_plaatsen():
                    vertoning.start()
                    print(str(tickets),"Tickets geaccepteerd voor vertoning " + str(vertoning_id) + "!")
                    print("\033[1;35mVertoning met id: \033[0m" + str(vertoning_id) + " \033[1;35mis gestart!\033[0m")
                    return True
                print(str(tickets),"Tickets geaccepteerd voor vertoning " + str(vertoning_id) + "!")
                return True
            else:
                print(str(tickets) + "\033[1;31m mensen kunnen niet Vertoning: \033[0m" + str(
                    vertoning_id) + "\033[1;31m bekijken! (Geen Reservatie)\033[0m")
                return False
        else:
            print(str(tickets) + "\033[1;31m mensen kunnen niet Vertoning: \033[0m" + str(vertoning_id) + "\033[1;31m bekijken! (Geen Reservatie)\033[0m")
            return False
    def vertoningInfo(self):
        films = self.getFilms()
        vertoningen = self.getVertoningen()
        datum_film = []
        for vertoning in vertoningen:
            zaal, zaal_bestaat = self.getZaal(vertoning.get_zaalnummer())
            for film in films:
                if vertoning.filmid == film.id:
                    datum_film.append\
                    (
                        tuple
                        ((
                            vertoning,
                            str(vertoning.datum.date()),
                            film.get_titel(),
                            "Screening: " + str(vertoning.id),
                            str(vertoning.slot),
                            str(vertoning.get_plaatsenbezet()),
                            zaal
                        ))
                    )
        return datum_film

    def log(self,tijd):
        datum_film = self.vertoningInfo()
        nummer_vertoning = []
        datum = []
        zaal = []
        filmslist = []
        _11u00 = []
        _14u30 = []
        _17u00 = []
        _20u00 = []
        _22u30 = []
        def voegF_Toe(nm,tickets,slotFinal,slot1, slot2, slot3, slot4):
            for x in nummer_vertoning:
                if nm == x:
                    slotFinal.append("F:" + str(tickets))
                    slot1.append(" ")
                    slot2.append(" ")
                    slot3.append(" ")
                    slot4.append(" ")
        def voegG_Toe(vert,zl,nm,slotFinal,slot1, slot2, slot3, slot4):
            for x in nummer_vertoning:
                if nm == x:
                    slotFinal.append("G:" + str(zl.get_plaatsen() - vert.get_vrije_plaatsen()))
                    slot1.append(" ")
                    slot2.append(" ")
                    slot3.append(" ")
                    slot4.append(" ")
        def voegW_Toe(vert,zl,nm,slotFinal,slot1, slot2, slot3, slot4):
            for x in nummer_vertoning:
                if nm == x:
                    slotFinal.append("W:" + str(zl.get_plaatsen() - (vert.get_plaatsenbezet() + vert.get_vrije_plaatsen())))
                    slot1.append(" ")
                    slot2.append(" ")
                    slot3.append(" ")
                    slot4.append(" ")

        def voegF_toe(slot,nm, tickets):
            if slot == "11:00:00":
                voegF_Toe(nm, tickets, _11u00, _14u30, _17u00, _20u00, _22u30)
            elif slot == "14:30:00":
                voegF_Toe(nm, tickets, _14u30, _11u00, _17u00, _20u00, _22u30)
            elif slot == "17:00:00":
                voegF_Toe(nm, tickets, _17u00, _14u30, _11u00, _20u00, _22u30)
            elif slot == "20:00:00":
                voegF_Toe(nm, tickets, _20u00, _14u30, _17u00, _11u00, _22u30)
            elif slot == "22:30:00":
                voegF_Toe(nm, tickets, _22u30, _14u30, _17u00, _20u00, _11u00)
        def voegG_toe(slot,vert,zl,nm):
            if slot == "11:00:00":
                voegG_Toe(vert, zl, nm, _11u00, _14u30, _17u00, _20u00, _22u30)
            elif slot == "14:30:00":
                voegG_Toe(vert, zl, nm, _14u30, _11u00, _17u00, _20u00, _22u30)
            elif slot == "17:00:00":
                voegG_Toe(vert, zl, nm, _17u00, _14u30, _11u00, _20u00, _22u30)
            elif slot == "20:00:00":
                voegG_Toe(vert, zl, nm, _20u00, _14u30, _17u00, _11u00, _22u30)
            elif slot == "22:30:00":
                voegG_Toe(vert, zl, nm, _22u30, _14u30, _17u00, _20u00, _11u00)
        def voegW_toe(slot,vert, zl, nm):
            if slot == "11:00:00":
                voegW_Toe(vert, zl, nm, _11u00, _14u30, _17u00, _20u00, _22u30)
            elif slot == "14:30:00":
                voegW_Toe(vert, zl, nm, _14u30, _11u00, _17u00, _20u00, _22u30)
            elif slot == "17:00:00":
                voegW_Toe(vert, zl, nm, _17u00, _14u30, _11u00, _20u00, _22u30)
            elif slot == "20:00:00":
                voegW_Toe(vert, zl, nm, _20u00, _14u30, _17u00, _11u00, _22u30)
            elif slot == "22:30:00":
                voegW_Toe(vert, zl, nm, _22u30, _14u30, _17u00, _20u00, _11u00)


        for vert,dat,film,nm,slot,tickets,zl in datum_film:
            zaal.append(zl.nummer)
            nummer_vertoning.append(nm)
            datum.append(dat)
            filmslist.append(film)
            d = datetime
            # FILM IS BEZIG
            if vert.is_bezig():
                voegF_toe(slot,nm,tickets)
            # ZAAL IS HELEMAAL LEEG EN VERTONING IS AL VOORBIJ
            elif vert.get_vrije_plaatsen() == zl.get_plaatsen() and timer.getTime() >= d.combine(vert.get_datum(), vert.get_slot()) :
                voegF_toe(slot,nm,tickets)
            # ZAAL IS HELEMAAL LEEG EN VERTONING IS NOG NIET VOORBIJ
            elif vert.get_vrije_plaatsen() == zl.get_plaatsen() and timer.getTime() < d.combine(vert.get_datum(), vert.get_slot()):
                voegG_toe(slot,vert,zl,nm)
            # ZAAL IS AAN HET WACHTEN VOOR MENSEN
            elif vert.aan_het_wachten():
                voegW_toe(slot,vert,zl,nm)
            else:
                voegG_toe(slot,vert,zl,nm)

        tabel = \
        {
            'Film Screening': nummer_vertoning,
            'Zaal': zaal,
            'Date': datum,
            'Film': filmslist,
            '11.00': _11u00,
            '14.30': _14u30,
            '17.00': _17u00,
            '20.00': _20u00,
            '22.30': _22u30
        }

        my_data = pd.DataFrame(data=tabel)
        html = my_data.to_html(index=False)

        css = '''
        <style>
        body {
            background-color: #4444FF;
            font-family: Arial, Helvetica, sans-serif;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
        }

        th {
            background-color: #FF1744;
            color: white;
            font-weight: bold;
            text-align: center;
            padding: 16px;
            font-size: 20px;
        }

        th:first-child {
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        }

        th:last-child {
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        }

        td {
            border: 1px solid black;
            padding: 16px;
            font-size: 18px;
            text-align: center;
        }

        tr:nth-child(even) {
            background-color: #909090 ;
        }
        </style>
        '''

        adm = admin.upper()
        begin = f"<div style='text-align:center; font-family: Calisto MT, sans-serif; font-size: 28px; color: #FF3396;'> {adm}'S LOG: {tijd} </div>"
        with open("kinepolis_logo.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        image_html = f'<div style="text-align:center;padding-top:50px;"><img src="data:image/png;base64,{encoded_string}" style="max-width: 150px; height: auto;"/></div>'
        full_html = f"<html><head>{css}</head><body>{html}<br>{begin}{image_html}</body></html>"
        with open('log.html', 'w') as f:
            f.write(full_html)
