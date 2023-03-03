
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


    def vind_zaal(self,zaalnummer):
        """
        zoekt door de ketting met zalen op de zaalnummer. Als de zaal bestaat returnt
        die de zaal nummer en aantal plaatsen als een tuple. als deze niet bestaat return een error.
        :param zaalnummer: De unieke nummer van de zaal.
        :return: returnt tuple met zaalnummer en aantal plaatsen.
        """
        return str(zaalnummer)


    def kom_binnen(self,Reservatie):
        """
        Zorgt ervoor dat er iemand in een zaal kan als die gereserveerd heeft. hierdoor is er een plaats minder is.
        :param Reservatie: de reservatie van iemand
        :return: true als de persoon binnen is.
        """

    def zaal_vol(self):
        """
        de zaal is vol dus niemand kan er nog bij.
        :return: de zaal is vol sorry.
        """


    # def get_zaalnummer(self):
    #     """
    #     Geeft de nummer terug van de zaal die aangemaakt was.
    #     :return: de zaal nummer als int
    #     """
    #     return self.nummer
    #
    # def get_plaatsen(self):
    #     """
    #     geeft het aantal plaatsen terug van de zaal die aangemaakt was.
    #     :return: het aantal plaatsen als int
    #     """
    #     return self.plaatsen
