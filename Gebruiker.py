import Reservatiesysteem
class Gebruiker:
    ##data
    def __init__(self):
        self.id = None #nog geen id gekent
        self.voornaam = None #nog geen voornaamgekent
        self.achternaam = None #nog geen achernaam gekent
        self.emailadres = None # nog geen emailadres gekent.
        self.state = False

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


        self.id = id  # nog geen id gekent
        self.voornaam = voornaam  # nog geen voornaamgekent
        self.achternaam = achternaam  # nog geen achernaam gekent
        self.emailadres = emailadres  # nog geen emailadres gekent.


    def verwijder_gebruiker(self,id):
        """
        deze zal de gebruiker verwijderen uit de ketting
        :param id: unieke string
        :return: true als verwijdert is.
        """

    def get_id(self):

        return self.id

    def get_voornaam(self):

        return self.voornaam

    def get_achternaam(self):

        return self.achternaam

    def get_emailadress(self):

        return self.emailadres

    def get_state(self):

        return self.state

    def zoek_gebruiker(self,id):
        """
        dit zoekt de gerbuiker op de unieke id
        :param id: unieke id
        :return: true als het gevonden is else false.
        """

        if id == self.id:
            return self.emailadres
        else:
            print("Geen gebruiker met deze " + str(id))

