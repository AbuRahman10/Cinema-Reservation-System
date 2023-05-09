from Ahmed_ADT.heap import *

class heapTable:
    def __init__(self):
        self.bst = Heap()

    def tableIsEmpty(self):
        return self.bst.heapIsEmpty()

    def tableInsert(self, value):
        return self.bst.heapInsert(value)

    def tableDelete(self, key):
        return self.bst.heapDelete(key)

    def tableRetrieve(self, key):
        return self.bst.heapRetrieve(key)

    def traverseTable(self, key = None):
        return self.bst.heapifyDown(key)

    def save(self):
        return self.bst.save()

    def load(self, a):
        self.bst.load(a)