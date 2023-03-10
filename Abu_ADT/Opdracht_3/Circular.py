class ListItemType:

    def __init__(self,item=None):
        """

        :param item: de value van elke node
        """
        self.item = item
        self.next = None
        self.prev = None

class LinkedChain:

    def __init__(self):
        """
        verbindt elke node met elkaar
        """
        self.size = 0
        self.head = None

    def isEmpty(self):
        """

        :return: true als de circulaire gelinkte lijst leeg is
        """
        if self.size == 0:
            return True
        return False

    def getLength(self):
        """

        :return: de lengte van de circulaire gelinkte lijst of eigenlijk het aantal nodes
        """
        return self.size

    def insert(self, index, newItem):

        """

        :param index: de gegeven index voor de nieuwe item die geplaatst moet worden
        :param newItem: de nieuwe item die geplaatst moet worden in de lijst (nieuwe node)
        :return: true als de newItem geplaatst is
        """
        if 0 < index <= self.size + 1:
            if self.isEmpty():
                self.head = ListItemType()
                self.head.item = newItem
                self.head.prev = None
                self.head.next = None
                self.size += 1
                return True

            elif index == 1:
                newNode = ListItemType()
                newNode.item = newItem
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode

                self.size += 1

                if self.size > 1:
                    lastnode = self.head
                    count = 0
                    while count != self.size - 1:
                        lastnode = lastnode.next
                        count += 1

                    lastnode.next = self.head
                    self.head.prev = lastnode

                return True

            elif index > 1 and index <= self.size:

                temp = self.head
                count = 0
                while count != index:
                    count += 1
                    if temp.next != None:
                        temp = temp.next

                newNode = ListItemType()
                newNode.item = newItem

                newNode.next = temp
                temp.prev.next = newNode
                newNode.prev = temp.prev
                temp.prev = newNode

                self.size += 1

                if self.size > 1:
                    lastnode = self.head
                    count = 0
                    while count != self.size - 1:
                        lastnode = lastnode.next
                        count += 1

                    lastnode.next = self.head
                    self.head.prev = lastnode

                return True

            elif index == self.size + 1:
                temp = self.head
                count = 0
                while count != self.size - 1:
                    count += 1
                    temp = temp.next

                newNode = ListItemType()
                newNode.item = newItem

                newNode.next = self.head
                temp.next = newNode
                newNode.prev = temp
                self.head.prev = newNode

                self.size += 1
            else:
                return False
        else:
            return False

    def save(self):
        """

        :return: de circulaire gelinkte lijst in een python list weergeven
        """
        savelijst = []
        eln = self.head
        count = 0
        while count != self.size:
            savelijst.append(eln.item)
            eln = eln.next
            count += 1

        return savelijst


    def retrieve(self,index):
        """

        :param index: gevraagde positie naar een node
        :return: true als de node op de gevraagde index verwijdert kan worden
        """
        if self.isEmpty():
            return None,False
        elif index < self.size + 1 and index > 0:

            current = self.head

            count = 1
            while count != index:
                count += 1
                if current.next != None:
                    current = current.next
            return current.item, True
        else:
            return None,False

    def delete(self,index):
        """

        :param index: gaat een node verwijderen op de gegeven index
        :return: true als de node verwijdert wordt van de circulaire gelinkte lijst
        """
        if 1 <= index <= self.size:
            if index == 1:
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1

                if self.size > 1:
                    lastnode = self.head
                    count = 0
                    while count != self.size - 1:
                        lastnode = lastnode.next
                        count += 1

                    lastnode.next = self.head
                    self.head.prev = lastnode

                return True
            elif index == self.size:
                temp = self.head
                count = 0
                while count != self.size:
                    count += 1
                    if temp.next != None:
                        temp = temp.next
                temp.prev.next = None
                self.size -= 1

                if self.size > 1:
                    lastnode = self.head
                    count = 0
                    while count != self.size - 1:
                        lastnode = lastnode.next
                        count += 1

                    lastnode.next = self.head
                    self.head.prev = lastnode

                return True
            else:
                temp = self.head
                count = 1
                while count != index:
                    count += 1
                    if temp.next != None:
                        temp = temp.next
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.size -= 1

                if self.size > 1:
                    lastnode = self.head
                    count = 0
                    while count != self.size - 1:
                        lastnode = lastnode.next
                        count += 1

                    lastnode.next = self.head
                    self.head.prev = lastnode

                return True

        else:
            return False

    def load(self,list):
        """

        :param list: gaat de elementen van list opslaan in een circulaire gelinkte lijst
        """
        for i in range(self.size - 1):
            self.delete(self.size)
            self.size -= 1


        list = list[::-1]
        for i in list:
            self.insert(1,i)

