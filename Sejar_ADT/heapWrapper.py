from Sejar_ADT.Heap import *

class heapTable:
    def __init__(self):
        self.heap = Heap()

    def tableIsEmpty(self):
        return self.heap.heapIsEmpty()

    def tableInsert(self, value):
        return self.heap.heapInsert(value)

    def tableDelete(self, key):
        return self.heap.heapDelete(key)

    def save(self):
        return self.heap.save()

    def load(self, a):
        self.heap.load(a)