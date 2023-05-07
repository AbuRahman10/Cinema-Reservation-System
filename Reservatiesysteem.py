import datetime

from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *
from Clock import timer
import pandas as pd

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
    from Abu_ADT.Opdracht_4.Hashmap.HashmapTable import *  # import general Linked Chain
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
            print(str(emailadres + " bestaat al!"))
            return False

        gebruiker.maak_gebruiker(id, voornaam, achternaam, emailadres)
        self.gebruikers.tableInsert((id, gebruiker)) # hier moeten we de object zelf inserten ipv input

        print("Gebruiker met id " + str(id) + " is gemaakt!")
        return True

    def addFilm(self, id, titel, rating):

        film = Film()

        for i in self.films.save():
            if i.id == id:
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
            if i.id == id:
                print("Vertoning ", id, " bestaat al!")
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
                print(str(zaalnummer) + " Bestaat al")
                return False

        zaal.maak_zaal(zaalnummer,plaatsen)
        if (self.zalen.tableInsert(self.indexZaal, zaal)):
            print("Zaal " + str(zaalnummer) + " is aangemaakt!")
            self.indexZaal += 1
        return True

    def getVertoning(self,id):
        return self.vertoningen.tableRetrieve(id)[1]

    def updateTickets(self, id_vertoning, tickets):
        vertoning, vertoning_bestaat = self.vertoningen.tableRetrieve(id_vertoning)

        if vertoning_bestaat:
            vertoning.plaatsenbezet += tickets
            zaal, zaal_bestaat = self.zalen.tableRetrieve(vertoning.get_zaalnummer())

            if zaal_bestaat and vertoning.get_plaatsenbezet() + vertoning.get_vrije_plaatsen() == zaal.get_plaatsen():
                vertoning.start()
            return True
        return False

    def buildLog(self, tijd):

        BeginHT = """
                <html>
        	<head>
        	<style>
        		table {
        		    border-collapse: collapse;
        		}

        		table, td, th {
        		    border: 1px solid #000000;
        		}
        	</style>
        </head>
        	<body>
        		<h1>Log op """ + tijd + """, met de ADTS van: """ + admin + """</h1>
        		<table>
        			<thead>
        				<td>Datum</td>
        				<td>Film</td>
        				<td>11:00</td>
        				<td>14:30</td>
        				<td>17:00</td>
        				<td>20:00</td>
        				<td>22:30</td>
        			</thead>
        			<tbody>
                """
        body = ""
        ENDHT = "</tbody></table></body></html>"
        with open("log.html", "w") as f:  # opent het output bestand om te schrijven
            f.write(BeginHT)  # schrijft BeginHT (formaat en standaardslots) in de output file
            films = []  # nieuwe lijst voor films
            #films.traverseTable(films.append) # zet alle films in films
            films = self.films.save()
            # for film in films:  # loopt over films
            #     titel = film.get_titel()  # krijg de titel van de film
            #     d = self.vertoningen.save()
            #     for day in self.vertoningen.save():  # loopt over elke dag van vertoningen van deze film
            #         body += self.buildTable(titel, day)  # voegt een nieuwe rij toe voor elke dag dat deze film wordt afgespeeld en voegt dit toe aan body
            f.write(body)  # schrijft de body in het output bestand
            f.write(ENDHT)  # schrijft ENDHT (einde file) in het output bestand

    def buildTable(self, titel, dag):
        slots = [datetime.time(11, 0), datetime.time(14, 30), datetime.time(17, 0), datetime.time(20, 0), datetime.time(22, 30)]  # standaard slots
        position_slot = 0  # index position_slot
        bfr = f"""
                            <tr>
                                <td>{dag[0].date()}</td>
                                <td>{titel}</td>
                                """
        for vertoning in dag[1]:  # loopt over de vertoningen van de dag
            while vertoning[0] != slots[position_slot]:  # Zolang er geen vertoning is op dit slot, wordt <td></td> bij de bfr toegevoegd
                bfr += f"<td></td>"  # geen vertoning
                position_slot += 1  # naar volgende positie gaan

            zaal, succes = self.zalen.tableRetrieve(vertoning[1].get_zaalnummer())  # zaal is 1ste element van de tuple, succes is het 2de element
            if not succes:  # kijkt na of zaal bestaat
                raise Exception("Zaal bestaat niet!")

            if vertoning[1].is_bezig():  # als de film gestart is
                bfr += f"<td>F:{vertoning[1].get_plaatsenbezet()}</td>"  # voeg "F: aantal mensen in zaal" toe aan bfr

            elif vertoning[1].get_vrije_plaatsen() == zaal.get_plaatsen() and datetime.datetime.combine(vertoning[1].get_datum(), vertoning[1].get_slot()) <= timer.getTime():
                bfr += f"<td>F:{vertoning[1].get_plaatsenbezet()}</td>"  # voeg "F: aantal mensen in zaal" toe aan bfr

            elif vertoning[1].get_vrije_plaatsen() == zaal.get_plaatsen() and datetime.datetime.combine(vertoning[1].get_datum(), vertoning[1].getSlot()) > timer.getTime():
                bfr += f"<td>G:{zaal.get_plaatsen() - vertoning[1].get_vrije_plaatsen()}</td>"  # voeg "G: aantal verkochte tickets" toe aan bfr

            elif vertoning[1].aan_het_wachten():  # als er gewacht moet worden op personen
                bfr += f"<td>W:{zaal.get_plaatsen() - (vertoning[1].get_plaatsenbezet() + vertoning[1].getAantalVrij())}</td>"  # voeg "W: aantal mensen waarop wachten" toe aan bfr

            else:
                bfr += f"<td>G:{zaal.get_plaatsen() - vertoning[1].get_vrije_plaatsen()}</td>"  # voeg "G: aantal verkochte tickets" toe aan bfr

            position_slot += 1  # ga naar volgende slot

        for p in range(position_slot, 5):  # voeg aan volgende slots <td></td> toe
            bfr += f"<td></td>"

        bfr += "</tr>"
        return bfr

    def log(self,tijd):
        tempfilms = self.films.save()
        vertoningen = self.vertoningen.save()
        datum = []
        filmslist = []
        datum_film = []
        for vertoning in vertoningen:
            for film in tempfilms:
                if vertoning.filmid == film.id:
                    datum_film.append(tuple((str(vertoning.datum.date()),film.get_titel())))
        result = list(dict.fromkeys(datum_film))
        for dat,film in result:
            datum.append(dat)
            filmslist.append(film)
        tabel = {
            'Datum': datum,
            'Film': filmslist,
            '11.00': " ",
            '14.30': " ",
            '17.00': " ",
            '20.00': " ",
            '22.30': " "
        }
        my_data = pd.DataFrame(data=tabel)
        my_data.to_html('log.html', index=False)
