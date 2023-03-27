import math

from Abu_ADT.Opdracht_3.Circular import *

def createTableItem(key,val):
    return key

class Hashmap:
    def __init__(self,type,n):
        """
        type is een van "lin","quad","sep"
        n is de grootte van de hashmap
        """
        self.size = n
        self.type = type

        self.array = []

        if self.type == "sep":
            for none in range(n):
                ketting = LinkedChain()
                self.array.append(ketting)
        else:
            for none in range(n):
                self.array.append(None)

    def isEmpty(self):

        if self.type == "sep":
            for i in self.array:
                if not i.isEmpty():
                    return False
            return True
        else:
            for i in self.array:
                if i is not None:
                    return False
            return True

    def modulo(self,key):
        """

        :param key: de gegeven item die je gaat inserten
        :return: de hashfunctie berekenen (modulo berkenen)
        """
        return key % self.size

    def arrayFull(self):

        if self.type == "sep":
            for i in self.array:
                if i.isEmpty():
                    return False
            return True
        else:
            for i in self.array:
                if i is None:
                    return False
            return True

    def linear_prob(self,pos,key):
        while pos < self.size:
            if self.array[pos] == None:  # vak is vrij
                self.array[pos] = key
                return True
            else:
                pos += 1

        pos = 0

        while pos < self.size:
            if self.array[pos] == None:  # vak is vrij
                self.array[pos] = key
                return True
            else:
                pos += 1

    def linear_probRetrieve(self,pos,item):
        while pos < self.size:
            if self.array[pos] == item:  # vak is vrij
                return self.array[pos],True
            else:
                pos += 1

        pos = 0

        while pos < self.size:
            if self.array[pos] == item:  # vak is vrij
                return self.array[pos], True
            else:
                pos += 1

        return None,False

    def linear_probDelete(self,pos,keyType):
        while pos < self.size:
            if self.array[pos] == keyType:  # vak is vrij
                self.array[pos] = None
                return True
            else:
                pos += 1

        pos = 0

        while pos < self.size:
            if self.array[pos] == keyType:  # vak is vrij
                self.array[pos] = None
                return True
            else:
                pos += 1

        return False

    def quadratic_prob(self,pos,key):

        j = 0
        while self.array[pos] is not None:
            j += 1
            pos = int(self.modulo(key + math.pow(j,2)))

        self.array[pos] = key
        return True

    def quadratic_probRetrieve(self,pos,item):
        j = 0
        while self.array[pos] is not item:
            j += 1
            pos = int(self.modulo(item + math.pow(j,2)))
            if j == self.size + 1:
                return None,False

        return self.array[pos],True

    def quadratic_probDelete(self,pos,keyType):

        j = 0
        while self.array[pos] is not keyType:
            j += 1
            pos = int(self.modulo(keyType + math.pow(j,2)))
            if j == self.size * 2:
                return False

        self.array[pos] = None
        return True

    def separate_chain(self,pos,key):

        self.array[pos].insert(1,key)
        return True

    def separate_chainRetrieve(self,pos,item):

        for count in range(1,self.array[pos].getLength() + 1):
            if self.array[pos].retrieve(count)[0] == item:
                return self.array[pos].retrieve(count)[0],True
        return None,False

    def separate_chainDelete(self, pos, keyType):

        for count in range(1,self.array[pos].getLength() + 1):
            i = self.array[pos].retrieve(count)[0]
            if self.array[pos].retrieve(count)[0] == keyType:
                return self.array[pos].delete(count)
        return False

    def tableInsert(self,key):

        if not self.arrayFull():
            positie = self.modulo(key)
            if positie < self.size:
                if self.type == "lin":
                    return self.linear_prob(positie,key)
                elif self.type == "quad":
                    return self.quadratic_prob(positie,key)
                elif self.type == "sep":
                    return self.separate_chain(positie,key)
        return False

    def tableRetrieve(self,item):
        position = self.modulo(item)
        if position < self.size:
            if self.type == "lin":
                if self.array[position] == None:
                    return None, False
                else:
                    return self.linear_probRetrieve(position,item)
            elif self.type == "quad":
                if self.array[position] == None:
                    return None, False
                else:
                    return self.quadratic_probRetrieve(position,item)
            elif self.type == "sep":
                if self.array[position].isEmpty():
                    return None, False
                else:
                    return self.separate_chainRetrieve(position,item)

    def tableDelete(self,keyType):
        position = self.modulo(keyType)
        if position < self.size:
            if self.type == "lin":
                if self.array[position] == None:
                    return False
                else:
                    return self.linear_probDelete(position, keyType)
            elif self.type == "quad":
                if self.array[position] == None:
                    return False
                else:
                    return self.quadratic_probDelete(position, keyType)
            elif self.type == "sep":
                if self.array[position].isEmpty():
                    return False
                else:
                    return self.separate_chainDelete(position, keyType)

    def save(self):

        if self.type == "lin" or self.type == "quad":
            output = {'type': self.type, 'items': self.array}
        else:
            output_list = []

            for i in self.array:
                if i.isEmpty():
                    output_list.append(None)
                else:
                    output_list.append(i.save())

            output = {'type': self.type, 'items': output_list}

        return output

    def load(self,hashTable):
        self.array.clear()
        self.type = hashTable['type']


        if self.type == 'lin' or self.type == 'quad':
            self.array = hashTable['items']
            self.size = len(hashTable['items'])
        else:
            self.array.clear()
            templist = hashTable['items']
            for i in templist:
                if i is None:
                    ketting = LinkedChain()
                    self.array.append(ketting)
                else:
                    ketting2 = LinkedChain()
                    ketting2.load(i)
                    self.array.append(ketting2)
            self.size = len(hashTable['items'])
