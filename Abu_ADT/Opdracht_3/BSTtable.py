from BST import *

class BSTTable:

    def __init__(self):
        """
        maakt een bst object
        """
        self.myBST = BST()

    def tableIsEmpty(self):
        """

        :return: true als de bst leeg is
        """
        return self.myBST.isEmpty()

    def tableInsert(self,keyType):
        """

        :param keyType: item die geplaatst moet worden in de bst
        :return: true als het plaatsen mogelijk is
        """
        return self.myBST.searchTreeInsert(keyType)

    def tableRetrieve(self,keyType):
        """

        :param keyType: item die de user vraagt van de boom
        :return: true als de item bestaat in de bst en de item zelf
        """
        return self.myBST.searchTreeRetrieve(keyType)

    def traverseTable(self,print):
        """

        :return: gaat op inorder wijze de bst printen
        """
        self.myBST.inorderTraverse(print)

    def save(self):
        """

        :return: de bst in een mooie dictionary
        """
        return self.myBST.save()

    def load(self,dict):
        """

        :param dict: de gekregen dictionary (opslaan in een bst)
        """
        self.myBST.load(dict)

    def tableDelete(self,keyType):
        """

        :param keyType: item die verwijdert moet worden uit de bst
        :return: true als het verwijderen mogelijk is
        """
        return self.myBST.searchTreeDelete(keyType)

