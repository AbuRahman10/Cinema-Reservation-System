class Node:
# De node van onze ketting
    def __init__(self, data, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data


class LinkedChain:
	# lege ketting initialiseren.
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def isEmpty(self):
        # een ketting is leeg wanneer de hoofd Node , oftewel de eerste Node leeg is.
        if self.head is None:
            return True
        return False

    def getLength(self):
        return self.lenght


    def insert(self, pos, data):
        # check of de gewenste inserting positie wel tussen de juiste waarden ligt;
        if pos <= 0 or pos > self.lenght + 1:
            return False
        # maak een nieuwe node aan voor de insert.
        newNode = Node(data)
        #als de ketting leeg is dan is de head en de tail gelijk aan de nieuwe node van de insert.
        if self.isEmpty():
            self.head = self.tail = newNode
            newNode.next = newNode.prev = self.head
            # als insert moet gebeuren in de head, dan wordt de nieuwe node de head node , en wordt de prev pointer van de nieuwe head node de voirge tail node en de next wordt de pointer naar de vorige head node.
        elif pos == 1:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        # inserting at the tail: de nieuwe node's pointer naar de prev wordt gezet op de huidige tail, de next pointer wijst naar de huidige head, en de nieuwe tail wordt dus de nieuwe Node
        elif pos == self.lenght + 1:
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.head.prev = newNode
            self.tail = newNode
        else:
            huidig = self.head
            for i in range(pos - 2):
                huidig = huidig.next
            newNode.next = huidig.next
            newNode.prev = huidig
            huidig.next.prev = newNode
            huidig.next = newNode
        self.lenght += 1
        return True

    def retrieve(self, i):
        # check of de index in de juiste range zit
        if i <= 0 or i > self.lenght:
            return (None, False)
        huidig = self.head
        for i in range(i):
            huidig = huidig.next
        return (huidig.data, True)
    # geef de element terug op positie i.

    def save(self):
        # slaagt de ketting op als een lijst
        chain = []
        current = self.head
        for i in range(self.lenght):
            data = current.data
            chain.append(data)
            current = current.next
        return chain


    def load(self, val):
        # inserten in de lijst van de ketting
        if val is None:
            return False
        self.lenght = 0
        self.head = None
        for j in range(len(val)):
            self.insert(j + 1, val[j])

    def delete(self, pos):
        # verwijdert een elemement van de ketting op een bepaalde positie.
        if self.isEmpty() or pos > self.lenght or pos <= 0:
            return False

        current = self.head
        if pos == 1:
            self.head = current.next
            current.next.prev = current.prev
            current.prev.next = current.next
            self.lenght -= 1
            return True

        for i in range(pos - 2):
            current = current.next

        current.next = current.next.next
        current.next.prev = current
        self.lenght -= 1
        return True