from datetime import datetime
from Clock import timer

class Vertoning:
    ##data
    def __init__(self):
        self.id = None #nog geen id toegekent
        self.zaalnummer = None #nog geen zaalnummer aan toegekent
        self.slot = None #nog geen tijdslot aan toegevoegd.
        self.datum = None #nog geen datum aan toegekent
        self.filmid = None #nog geen filmid aan toegekent.
        self.vrijeplaatsen = None #vrijplaatsen nog niet bekent
        self.bezig = False
        self.plaatsenbezet = 0

    ##functionalteit
    def maak_vertoning(self,id,zaalnummer,slot,datum,filmid, vrijeplaatsen):
        """
        maakt een film aan met een id, op een zaalnummer, met een bepaald tijdsslot,
        op een bepaalde datum, met een bepaald filmid.
        preconditie: id,zaalnummer,slot,filmid zijn integers en datum is een string.
        postconditie: de film wordt aangemaakt op een plaats in de Bst op het id
        :param id: een interger die het id geeft
        :param zaalnummer: een int die de zaal nummer geeft
        :param slot: een int als tijdslot
        :param datum: een string als datum
        :param filmid: een int die het id van de film weergeeft
        :return: true als het toegevoegd is aan de BST
        """
        self.id = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.vrijeplaatsen = vrijeplaatsen


    def get_id(self):

        return self.id

    def get_zaalnummer(self):

        return self.zaalnummer

    def get_datum(self):

        return self.datum

    def get_slot(self):

        return self.slot

    def get_filmid(self):

        return self.filmid

    def get_vrije_plaatsen(self):

        return self.vrijeplaatsen

    def start(self):

        self.bezig = True

    def stop(self):

        self.bezig = False

    def is_bezig(self):

        return self.bezig

    def aan_het_wachten(self):

        return datetime.combine(self.datum, self.slot) <= timer.getTime() and not self.is_bezig()

    def get_plaatsenbezet(self):

        return self.plaatsenbezet

    def get_film(self,id):
        """
        vergeeft de film die in deze vertoning zit.
        :param Film: unieke string
        :return: de film.
        """
        if id == self.filmid:
            return id
        else:
            print("Geen film met deze " + str(id))