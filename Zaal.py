
class Zaal:
    ##data
    def __init__(self):
        self.nummer = None #nog geen nummer gegeven
        self.plaatsen = None #nog geen hoeveelheid plaatsen toegedient


    ##functionalteit
    def maak_zaal(self,zaalnummer,plaatsen):
        """
        slaagt de zalen op in een ketting met als zoeksleutel de zaalnummer.
        preconditie: er zal een zaalnummer zijn en een aantal plaatsen
        postconditie: de zaal zal toegevoegd worden aan de ketting.
        :param zaalnummer: een uniek nummer van de zaal
        :param plaatsen: een nummer voor het aantal plaatsen
        :return: True als het succesvol is toegevoegd aan de ketting
        """
        self.nummer = zaalnummer
        self.plaatsen = plaatsen

    def get_nummer(self):
        """
        Geeft de nummer terug van de zaal die aangemaakt was.
        :return: de zaal nummer als int
        """
        return self.nummer

    def get_plaatsen(self):
        """
        geeft het aantal plaatsen terug van de zaal die aangemaakt was.
        :return: het aantal plaatsen als int
        """
        return self.plaatsen
