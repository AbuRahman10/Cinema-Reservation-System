class Node:
    def __init__(self, data, volgende=None, vorige=None):
        self.volgende = volgende
        self.vorige = vorige
        self.data = data


class LinkedChain:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def insert(self, key, data):
        if key <= 0 or key > self.size + 1:
            return False
        nNode = Node(data)
        if self.isEmpty():
            self.front = self.back = nNode
            nNode.volgende = nNode.vorige = self.front
        elif key == 1:
            nNode.volgende = self.front
            nNode.vorige = self.back
            self.front.vorige = nNode
            self.back.volgende = nNode
            self.front = nNode
        elif key == self.size + 1:
            nNode.vorige = self.back
            nNode.volgende = self.front
            self.back.volgende = nNode
            self.front.vorige = nNode
            self.back = nNode
        else:
            huidig = self.front
            for i in range(key - 2):
                huidig = huidig.volgende
            nNode.volgende = huidig.volgende
            nNode.vorige = huidig
            huidig.volgende.vorige = nNode
            huidig.volgende = nNode
        self.size += 1
        return True

    def save(self):
        L = []
        huidig = self.front
        for i in range(self.size):
            data = huidig.data
            L.append(data)
            huidig = huidig.volgende
        return L

    def load(self, value):
        if value is None:
            return False
        self.size = 0
        self.front = None
        for j in range(len(value)):
            self.insert(j + 1, value[j])

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def getLength(self):
        return self.size

    def delete(self, key):
        if self.isEmpty() or key > self.size or key <= 0:
            return False

        huidig = self.front

        if key == 1:
            self.front = huidig.volgende
            huidig.volgende.vorige = huidig.vorige
            huidig.vorige.volgende = huidig.volgende
            self.size -= 1
            return True

        for i in range(key - 2):
            huidig = huidig.volgende

        huidig.volgende = huidig.volgende.volgende
        huidig.volgende.vorige = huidig
        self.size -= 1
        return True

    def retrieve(self, a):
        if a <= 0 or a > self.size:
            return (None, False)
        huidig = self.front
        for a in range(a):
            huidig = huidig.volgende
        return (huidig.data, True)

