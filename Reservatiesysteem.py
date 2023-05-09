import base64
import datetime
from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *
from Clock import timer
import pandas as pd
from IPython.display import Image


# Keuze Geadvanceerde ADT's
admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed : ")
admin = admin.lower()
admins = ["abu","sejar","ahmed"]


while admin not in admins:
    admin = input("Choice Advanced ADT's - Abu | Sejar | Ahmed : ")
    admin = admin.lower()

if admin == "abu":
    admin = "Abu"
    from Abu_ADT.Opdracht_4.Hashmap.LinkedChainTable import *
    from Abu_ADT.Opdracht_3.BSTtable import *
    from Abu_ADT.Opdracht_4.Hashmap.HashmapTable import *

elif admin == "sejar":
    admin = "Sejar"
    from Sejar_ADT.Heap import *
    from Sejar_ADT.BSTWrapper import *
    from Sejar_ADT.LinkedChainTable import *

elif admin == "ahmed":
    admin = "Ahmed"
    from Ahmed_ADT.heapWrapper import *
    from Ahmed_ADT.BSTWrapper import *
    from Ahmed_ADT.LinkedChainTable import *

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
        self.reservaties = LinkedChainTable()
        self.vertoningen = LinkedChainTable()

        # alleen bij LINKEDCHAIN!
        self.indexVertoning = 1
        self.indexFilm = 1
        self.indexReservatie = 1
        self.indexZaal = 1

    def addGebruiker(self, id, voornaam, achternaam, emailadres):

        gebruiker = Gebruiker()
        if self.gebruikers.tableRetrieve(id)[1]:
            print("\033[1;31mGebruiker met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
            return False

        gebruiker.maak_gebruiker(id, voornaam, achternaam, emailadres)
        self.gebruikers.tableInsert((id, gebruiker)) # hier moeten we de object zelf inserten ipv input

        print("Gebruiker met id " + str(id) + " is gemaakt!")
        return True

    def addFilm(self, id, titel, rating):

        film = Film()

        for i in self.films.save():
            if i.id == id or i.get_titel() == titel:
                print("\033[1;31mFilm met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
                return False

        film.voegfilmtoe(id, titel, rating)
        if (self.films.tableInsert(self.indexFilm, film)):
            self.indexFilm += 1
            print(titel + " is aangemaakt!")
        return True

    def addReservatie(self, timestamp, userid, vertoningid, aantalplaatsen):
        reservatie = Reservatie()

        vertoningen = self.vertoningen.save()
        vertoning =  Vertoning()
        bestaat = False
        for i in vertoningen:
            if i.id == vertoningid:
                vertoning = i
                bestaat = True
        if bestaat == False or vertoning.get_vrije_plaatsen() <= aantalplaatsen:
            return False
        aantal_vrij = vertoning.get_vrije_plaatsen() - aantalplaatsen  # het nieuwe aantal vrije plaatsen
        vertoning.vrijeplaatsen = aantal_vrij

        reservatie.maak_reservatie(timestamp, userid, vertoningid, aantalplaatsen)
        if (self.reservaties.tableInsert(self.indexReservatie, reservatie)):
            print("Reservatie van user " + str(userid) + " is aangemaakt!")
            self.indexReservatie += 1
        return True

    def addVertoning(self,id,zaalnummer,slot,datum,filmid, vrijePlaatsen):
        vertoning = Vertoning()

        showtimes = self.vertoningen.save()
        for i in showtimes:
            if i.id == id or (i.datum == datum and i.slot == slot and i.get_zaalnummer() == zaalnummer):
                print("\033[1;31mVertoning met id: \033[0m" + str(id) + " \033[1;31mis al gemaakt!\033[0m")
                return False

        vertoning.maak_vertoning(id,zaalnummer,slot,datum,filmid, vrijePlaatsen)
        if (self.vertoningen.tableInsert(self.indexVertoning,vertoning)):
            print("Vertoning " + str(id) + " is aangemaakt!")
            self.indexVertoning += 1
        return True

    def addZaal(self,zaalnummer,plaatsen):
        zaal = Zaal()

        zalen = self.zalen.save()
        for i in zalen:
            if i.nummer == zaalnummer:
                print("\033[1;31mZaal met id: \033[0m" + str(zaalnummer) + " \033[1;31mis al gemaakt!\033[0m")
                return False

        zaal.maak_zaal(zaalnummer,plaatsen)
        if (self.zalen.tableInsert(self.indexZaal, zaal)):
            print("Zaal " + str(zaalnummer) + " is aangemaakt!")
            self.indexZaal += 1
        return True

    def getVertoning(self,id):
        return self.vertoningen.tableRetrieve(id)[1]

    def updateTickets(self, vertoning_id, tickets):

        vertoning = Vertoning()
        zaal = Zaal()
        vertoning_bestaat = False
        zaal_bestaat = False
        vertoningen = self.vertoningen.save()
        zalen = self.zalen.save()

        for vtn in vertoningen:
            if vtn.id == vertoning_id:
                vertoning_bestaat = True
                vertoning = vtn

        if vertoning_bestaat:
            vertoning.plaatsenbezet += tickets
            for zl in zalen:
                if zl.nummer == vertoning.get_zaalnummer():
                    zaal_bestaat = True
                    zaal = zl
            if zaal_bestaat and vertoning.get_plaatsenbezet() + vertoning.get_vrije_plaatsen() == zaal.get_plaatsen():
                vertoning.start()
            return True
        return False

    def log(self,tijd):
        films = self.films.save()
        vertoningen = self.vertoningen.save()
        zalen = self.zalen.save()

        datum_film = []
        for vertoning in vertoningen:
            zaal = Zaal()
            for zl in zalen:
                if zl.nummer == vertoning.get_zaalnummer():
                    zaal = zl
            for film in films:
                if vertoning.filmid == film.id:
                    tup = tuple\
                    (
                        (
                            vertoning,str(vertoning.datum.date()),
                            film.get_titel(),"Screening: " + str(vertoning.id),
                            str(vertoning.slot),
                            str(vertoning.get_plaatsenbezet()),
                            zaal
                         )
                    )
                    datum_film.append(tup)

        nummer_vertoning = []
        datum = []
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
            nummer_vertoning.append(nm)
            datum.append(dat)
            filmslist.append(film)
            d = datetime
            if vert.is_bezig():
                voegF_toe(slot,nm,tickets)
            elif vert.get_vrije_plaatsen() == zl.get_plaatsen() and d.combine(vert.get_datum(), vert.get_slot()) <= timer.getTime():
                voegF_toe(slot,nm,tickets)
            elif vert.get_vrije_plaatsen() == zl.get_plaatsen() and d.combine(vert.get_datum(),vert.get_slot()) > timer.getTime():
                voegG_toe(slot,vert,zl,nm)
            elif vert.aan_het_wachten():
                voegW_toe(slot,vert,zl,nm)
            else:
                voegG_toe(slot,vert,zl,nm)



        # define the table and style as before
        tabel = {
            'Film Screening': nummer_vertoning,
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

        with open("kinepolis_logo.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        # Embed the image in the HTML code
        image_html = f'<div style="text-align:center;padding-top:50px;"><img src="data:image/png;base64,{encoded_string}" style="max-width: 150px; height: auto;"/></div>'

        # Combine the HTML code and the image code
        full_html = f"<html><head>{css}</head><body>{html}<br>{image_html}</body></html>"

        # write the output to a file
        with open('log.html', 'w') as f:
            f.write(full_html)
