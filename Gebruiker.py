
class Gebruiker:
    ##data
    def __init__(self):
        self.id = None #nog geen id gekent
        self.voornaam = None #nog geen voornaamgekent
        self.achternaam = None #nog geen achernaam gekent
        self.emailadres = None # nog geen emailadres gekent.

    ##functionaliteit
    def maak_gebruiker(self,id ,voornaam,achternaam,emailadres):
        """
        er wordt er een gebruiker aan gemaakt. op een id die een voornaam, achternaam, emailheeft.
        preconditie: er bestaat nog niets dus de BST is ook nog leeg.
        postconditie: de bst is een persoon groter.
        :param id: een int
        :param voornaam: een string
        :param achternaam:een string
        :param emailadres: een string als email.
        :return: return true als de gerbuiker toegevoegd is.
        """
        pass

    def verwijder_gebruiker(self,id):
        """
        deze zal de gebruiker verwijderen uit de ketting
        :param id: unieke string
        :return: true als verwijdert is.
        """

    def zoek_gebruiker(self,id):
        """
        dit zoekt de gerbuiker op de unieke id
        :param id: unieke id
        :return: true als het gevonden is else false.
        """