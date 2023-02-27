class StackItemType:
    """
    Dit is het type van de nieuwe item
    """
    def __init__(self, value):
        """
        :param value: uw item
        """
        self.value = value


class MyStack:

    def __init__(self,max_size):
        """
        Creëert een lege stack.

        preconditie: max_size > 0
        postconditie: er is een stack aangemaakt en die is leeg (size == 0)

        :param max_size: dit is de maximum grootte van de stack
        """
        self.items = [None] * max_size
        self.size = 0


    def isEmpty(self):
        """
        gaat bepalen of een stack leeg is

        :param: self
        :return: Boolean
        """
        if self.size == 0:
            return True
        else:
            return False

    def push(self, newItem):

        """
        voegt een element toe aan de stack

        preconditie: de stack size is niet vol, anders geen nieuwe element toegevoegd
        postconditie: er zit een element meer in de stack
        :param newItem: dat is het nieuwe item
        :return: Boolean
        """

        if self.size == len(self.items):
            return False
        self.items[self.size] = newItem
        self.size += 1
        return True

    def pop(self):
        """
        verwijdert het laatst toegevoegde element uit de stack

        preconditie: de stack size is niet vol, anders geen element verwijderd
        postconditie: de laatste element is verwijderd

        :param: self
        :return: top item van de stack, bool
        """
        if self.isEmpty():
            return False, False
        stackTop = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        return stackTop, True

    def getTop(self):
        """
        vraagt het laatst toegevoegde element uit de stack op

        :param: self
        :return: top van de stack, bool
        """
        if self.isEmpty():
            return False, False
        else:
            return self.items[self.size - 1], True


    def save(self):

        savelijst = []

        for eln in self.items:
            if eln != None:
                savelijst.append(eln)

        return savelijst

    def load(self,list):

        self.items = list
        self.size = len(list)



if __name__ == "__main__":
    s = MyStack(2)
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.push(1))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())
    print()

    s.load(['a','b','c'])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())












