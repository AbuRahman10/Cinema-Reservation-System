from typing import Any


class Reservatie:
    ##data
    def __init__(self):
        self.userid = None # nog geen user id
        self.timestamp = None #nog geen timpstamp
        self.vertoningid = None #nog geen vertonings id
        self.aantalplaatsen = None #nog geen aantal plaatsen gereserveerd

    ##functionalteit
    def maak_reservatie(self,timestamp,userid,vertoningid,aantalplaatsen):
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

        self.userid = userid
        self.timestamp = timestamp
        self.vertoningid = vertoningid
        self.aantalplaatsen = aantalplaatsen

    def getUserid(self):
        return self.userid

    def getTimestamp(self):
        return self.timestamp

    def getVertoningid(self):
        return self.vertoningid

    def getPlaatsen(self):
        return self.aantalplaatsen

