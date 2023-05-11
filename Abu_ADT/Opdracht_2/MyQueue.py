class StackItemType:
    """
    Dit is het type van de nieuwe item
    """
    def __init__(self, value):
        """
        :param value: uw item
        """
        self.value = value


class MyQueue:

    def __init__(self,max_size=200):
        """
        Creëert een lege queue.

        preconditie: max_size > 0
        postconditie: er is een queue aangemaakt en die is leeg (size == 0)

        :param max_size: dit is de maximum grootte van de queue
        """
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        """
        gaat bepalen of een queue leeg is

        :param: self
        :return: Boolean
        """
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, newItem):

        """
        voegt een element toe aan de queue

        preconditie: de queue size is niet vol, anders geen nieuwe element toegevoegd
        postconditie: er zit een element meer in de queue
        :param newItem: dat is het nieuwe item
        :return: Boolean
        """

        if self.size == len(self.items):
            return False
        self.items[self.size] = newItem
        self.size += 1
        return True

    def dequeue(self):

        """
        verwijdert het laatst toegevoegde element uit de stack

        preconditie: de stack size is niet vol, anders geen element verwijderd
        postconditie: de laatste element is verwijderd

        :param: self
        :return: top item van de stack, bool
        """
        if self.isEmpty():
            return False, False
        queueFront = self.items[0]
        self.items[0] = None

        templ = []

        counter = 0

        for element in self.items:
            if element != None:
                templ.append(element)
            else:
                counter += 1
        for count in range(counter):
            templ.append(None)

        self.items = templ

        self.size -= 1
        return queueFront, True

    def getFront(self):
        """
        vraagt het laatst toegevoegde element uit de stack op

        :param: self
        :return: top van de stack, bool
        """
        if self.isEmpty():
            return None, False
        else:
            return self.items[0], True

    def save(self):

        savelijst = []

        for eln in self.items:
            if eln != None:
                savelijst.append(eln)

        return savelijst[ : :-1]

    def load(self,list):

        self.items = list[ : :-1]
        self.size = len(list)


if __name__ == "__main__":
    q = MyQueue(10)
    print(q.isEmpty())
    print(q.getFront()[1])
    print(q.dequeue()[1])
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.isEmpty())
    print(q.dequeue()[0])
    q.enqueue(5)
    print(q.save())

    print()

    q.load(['a', 'b', 'c'])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())






