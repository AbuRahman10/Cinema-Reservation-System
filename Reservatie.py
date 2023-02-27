class Reservatie:
    ##data
    def __init__(self):
        self.id = None #nog geen reservatie id
        self.userid = None # nog geen user id
        self.timestamp = None #nog geen timpstamp
        self.vertoningid = None #nog geen vertonings id
        self.aantalplaatsen = None #nog geen aantal plaatsen gereserveerd

    ##functionalteit
    def maak_reservatie(self,id,userid,timestamp,vertoningid,aantalplaatsen):
        """
        hiermaak je een reservatie aan en sla je deze op in een ketting. deze ketting
        blijft ook bestaan zodat je reservaties altijd terug kan vinden.
        preconditie: de user heeft een ID en op deze id voeg je de vertonigs id en en aantal plaatsen toen.
        postcoditie: return true als de reservatie succesvol was
        :param id: een interger
        :param userid: een unieke intergeer
        :param timestamp: een tuple met datum en tijd
        :param vertoningid: een unieke int van de vertoning
        :param aantalplaatsen: een int voor het aantal plaatsen
        :return: true als het succesvol was.
        """

    def get_zaal(self):
        """
        hier zoekt men de zaal die bij de reservatie hoort. Hierdoor kan mn de zaal returnen
        :return: de zaal nummer.
        """
        pass

    def verwijder_reservatie(self,id):
        """
        verwijderde reservatie op id. hierdoor wordt deze id vrij gegevenen en uit de ketting gehaald.
        :param id: unieke string
        :return: true als het succesvol verwijdert is.
        """

    def zoek_reservatie(self,id):
        """
        zoekt op de unieke id naar de film
        :param id: unieke string
        :return: true als het gevonden is else false.
        """