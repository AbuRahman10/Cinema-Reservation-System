# Maak een circulaire dubbelgelinkte ketting

class Node:
    def __init__(self, value):
        self.index = None
        self.data = value
        self.prev = None
        self.next = None

    def insert(self, index, value):
        if isinstance(self, TestNode):
            return [2, False]
        elif self.index == index - 1 and isinstance(self.next, TestNode):
            newNode = Node(value)
            newNode.index = index
            newNode.next = self.next
            newNode.prev = self
            self.next.prev = newNode
            self.next = newNode
            return [1, True]
        elif self.index == index:
            newNode = Node(value)
            newNode.index = self.index
            self.plus_een()
            newNode.prev = self.prev
            self.prev.next = newNode
            newNode.next = self
            self.prev = newNode
            return [0, True]
        elif self.index < index:
            if isinstance(self.next, TestNode) is False:
                returnValue = self.next.insert(index, value)
                return returnValue
        elif self.index > index:
            if isinstance(self.prev.prev, TestNode) is False:
                returnValue = self.prev.prev.insert(index, value)
                return returnValue
        else:
            return [2, False]

    def plus_een(self):
        if isinstance(self, TestNode) is False:
            self.index = self.index + 1
            if isinstance(self.next, TestNode) is False:
                self.next.plus_een()

    def min_een(self):
        if isinstance(self, TestNode) is False:
            self.index = self.index - 1
            if isinstance(self.next, TestNode) is False:
                self.next.min_een()

    def delete(self):
        self.min_een()
        self.prev.next = self.next
        self.next.prev = self.prev


    def deleteFind(self, index):
        if isinstance(self, TestNode):
            return False
        elif self.index == index:
            self.delete()
            return True
        elif self.index < index:
            if isinstance(self.next, TestNode) is False:
                returnValue = self.next.deleteFind(index)
                return returnValue
        else:
            return False

    def emptyChain(self):
        if isinstance(self, TestNode) is False:
            self.delete()
        if isinstance(self.next, TestNode) is False:
            self.next.emptyChain()


class TestNode:
    def __init__(self):
        self.index = 0
        self.next = None
        self.prev = None


class LinkedChain:
    def __init__(self):
        self.front = TestNode()
        self.back = self.front
        self.back.next = self.front
        self.front.prev = self.back
        self.back.prev = self.front

    def createList(self):
        self.front = TestNode()
        self.back = self.front
        self.front.index = 0
        self.back.next = self.front
        self.front.prev = self.back
        self.back.prev = self.front
        return True

    def destroyList(self):  # Functie die de lijst gaat verwijderen.
        del self
        return True


    def isEmpty(self):      # Functie die checkt of de LinkedChain leeg is.
        if isinstance(self.front.next, TestNode):
            return True
        else:
            return False


    def getLength(self):    # Functie die nakijkt wat de lengte van die LinkedChain is.
        count = 0
        countNode = self.front
        if self.front.next is not None:
            while countNode != self.back:
                count += 1
                countNode = self.front.next

        return count


    def delete(self, index):    # Functie die een gegeven index meekrijgt en de waarde verwijdert op die plek.
        if index != 0 and self.retrieve(index)[1] is True:
           if self.front.next is not None:
               returnValue = self.front.next.deleteFind(index)
               return returnValue

        return False

    def retrieve(self, index):  # Functie die de waarde teruggeeft op een de plaats van de gegeven index.
        if self.front.next is not None:
            curr = self.front.next
            while isinstance(curr.next, TestNode) is False:
                if curr.index == index:
                    return curr.data, True
                curr = curr.next
            if curr.index == index:
                return curr.data, True
            else:
                return index, False
        else:
            return index, False


    def insert(self, index, value):  # Functie die een gegeven waarde op een gegeven index gaat toevoegen in de LinkedChain.

        if isinstance(self.front.next, TestNode) is True and index == 1:
            self.front.next = Node(value)
            self.back = self.front.next
            self.front.next.prev = self.front
            self.front.next.next = self.front
            self.front.next.index = self.front.index + 1
            self.front.prev = self.front.next
            return True


        elif isinstance(self.front.next, TestNode) is False:
            returnResult = self.front.next.insert(index, value)
            if returnResult[0] == 1:
                curr = self.front
                if isinstance(self.front.next, TestNode) is False:
                    curr = self.front.next
                    while isinstance(curr.next, TestNode) is False:
                        curr = curr.next
                self.back = curr

            return returnResult[1]

        else:
            return False

    def load(self, list):   # Fuctie die een gegeven lijst meekrijgt en inlaad.
        if self.front.next is not None:
            self.front.next.emptyChain()
            self.back = self.front

        for dataElements in list:
            self.insert(list.index(dataElements) + 1, dataElements)


    def save(self):         # Functie die de LinkedChain gaat opslagen.
        L = []
        if self.front.next is not None:
            curr = self.front.next
            L.append(self.front.next.data)
            while isinstance(curr.next, TestNode) is False:
                curr = curr.next
                L.append(curr.data)

        return L
