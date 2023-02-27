from Abu_ADT.Opdracht_3.Circular import *

class LinkedChainTable:

    def __init__(self):

        self.myLinkedChain = LinkedChain()

    def tableIsEmpty(self):

        return self.myLinkedChain.isEmpty()

    def tableInsert(self,index,keyType):

        return self.myLinkedChain.insert(index,keyType)

    def tableRetrieve(self,index):

        return self.myLinkedChain.retrieve(index)

    def save(self):

        return self.myLinkedChain.save()

    def load(self,dict):

        return self.myLinkedChain.load(dict)

    def getLength(self):

        return self.myLinkedChain.getLength()