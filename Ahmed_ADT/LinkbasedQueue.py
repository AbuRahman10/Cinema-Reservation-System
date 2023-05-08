class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def getFront(self):
        if self.isEmpty():
            return None, False
        return self.head.data, True

    def enqueue(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return True

    def dequeue(self):
        if self.isEmpty():
            return None, False
        popped = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return popped, True

    def save(self):
        queue = []
        current = self.head
        while current is not None:
            queue.append(current.data)
            current = current.next
        return queue[::-1]

    def load(self, data):
        self.head = None
        self.tail = None
        for i in range(len(data)-1, -1, -1):
            self.enqueue(data[i])
        return self.head,True