from Ahmed_ADT.LinkbasedQueue import *

class queueTable:
    def __init__(self):
        self.queue = MyQueue()

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableInsert(self, value):
        return self.queue.enqueue(value)

    def tableDelete(self, key):
        return self.queue.dequeue()

    def save(self):
        return self.queue.save()

    def load(self, a):
        self.queue.load(a)