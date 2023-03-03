class Film:
    ##data
    def __init__(self):
        self.id = None #nog geen film ID toegekent
        self.titel = None #nog geen titel toegekent
        self.rating = None #nog geen rating toegekent aan de film.

    ##functionalteit
    def voegfilmtoe(self,id,titel,rating):
        """
        er wordt een film toegevoegd aan een BST van films.
        deze wordt toegevoegd op ID.
        preconditie: de Id is een interger, titel is een string, rating is een float.
        postcoditie: de ketting wordt 1 groter door toevoeging vande film.
        :param id: unieke int
        :param titel: een string
        :param rating: een float
        :return: returnt true als het toegevoed is aan de BST.
        """

        self.id = id  # nog geen film ID toegekent
        self.titel = titel  # nog geen titel toegekent
        self.rating = rating  # nog geen rating toegekent aan de film.

    def zoek_film(self,id):
        """
        er wordt gezocht door de BST van films
        preconditie: de film moet bestaan op dit ID als het niet bestaat returnt het niets.
        postconditie: als het gevonde is return de waarde van da ID als tuple
        :param id: is de integer waar op gezocht wordt.
        :return: waarde op de ID
        """
        return self.titel

    def verwijder_film(self,id):
        """
        De variabele wordt meegegeven als id van de film deze zal moeten verwijdert worden.
        :param id: string
        :return: true als deze succesvol verwijdert is.
        """


