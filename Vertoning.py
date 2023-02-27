class Vertoning:
    ##data
    def __init__(self):
        self.id = None #nog geen id toegekent
        self.zaalnummer = None #nog geen zaalnummer aan toegekent
        self.slot = None #nog geen tijdslot aan toegevoegd.
        self.datum = None #nog geen datum aan toegekent
        self.filmid = None #nog geen filmid aan toegekent.
        self.vrijeplaatsen = None #vrijplaatsen nog niet bekent

    ##functionalteit
    def maak_vertoning(self,id,zaalnummer,slot,datum,filmid):
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
        pass

    def get_vrijeplaatsen(self,Zaal):
        """
        roepen de functie aan in zaal de de tuple return voor de zaalnummer en aantal plaatsen.
        dan check je hoeveel keer deze film is gekozen is deze kleiner of gelijk aan het aantal plaatsen.
        neem de plaatsen - de hoeveelkeer gekozen. dat zijn de vrijeplaatsen.
        :param zaalnummer: een int die de zaal aanduid
        :return: de int van vrije plaatsen.
        """
        pass

    def get_film(self,Film):
        """
        vergeeft de film die in deze vertoning zit.
        :param Film: unieke string
        :return: de film.
        """
