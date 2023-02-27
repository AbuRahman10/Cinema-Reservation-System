from Hashmap import *

class HashmapTable:

    def __init__(self,string,n):
        """
        creërt een Hashmap object
        """

        self.myHashmap = Hashmap(string,n)

    def tableIsEmpty(self):

        """

        :return: true als de hashmap leeg is
        """
        return self.myHashmap.isEmpty()

    def tableInsert(self,newItem):
        """

        :param newItem: de item die geïnsert moet worden
        :return: true als de item geplaatst is in de map
        """
        return self.myHashmap.tableInsert(newItem)

    def tableRetrieve(self,item):
        """

        :param item: de item die geretrieved moet worden
        :return: true als de item in de map zit en returnt ook de item zelf
        """
        return self.myHashmap.tableRetrieve(item)

    def save(self):
        """

        :return: gaat de hashmap weergeven in een dictionary
        """
        return self.myHashmap.save()

    def load(self,hashTable):
        """

        :param hashTable: de gegeven dictionary
        :return: gaat de gegeven dictionary omvormen tot een hashmap en slaagt die op
        """
        self.myHashmap.load(hashTable)

    def tableDelete(self,keyType):
        """

        :param keyType: de item die verwijderd moet worden
        :return: true als de item succesvol verwijderd is
        """
        return self.myHashmap.tableDelete(keyType)

