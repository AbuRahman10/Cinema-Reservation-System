# Create class called 'Node'
class Node:
    def __init__(self, data):
        self.data = data
        self.after = None

    def getdata(self):
        return self.data

    def get(self):
        return self.after

    def set(self, after):
        self.after = after

# Create class called 'MyQueue'
class MyQueue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    # Check if queue is empty
    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        i = Node(data)
        if self.isEmpty():
            self.top = i
            self.bottom = i
            self.size += 1
            return True
        else:

            self.bottom.after = i
            self.bottom = i
            self.size += 1
            return True

    def dequeue(self):

        if self.isEmpty():
            return False, False
        else:
            item_to_remove = self.top

            if self.size == 1:
                self.top = None
                self.bottom = None
                self.size = 0

            else:
                self.top = self.top.get()
            self.size -= 1
            return item_to_remove.getdata(), True
    def getFront(self):
        if self.isEmpty():
            return False, False
        else:
            return self.top.getdata(), True

    def load(self, L):

        L = L[::-1]
        while self.top is not None:
            a = self.top
            self.top = self.top.get()
            a.set(None)
            a = None
            self.size -= 1

        for i in L:
            a = Node(i)
            b = self.top
            if self.top is None:
                self.top = a
            else:
                while b.get() is not None:
                    b = b.get()
                b.set(a)
                self.size += 1

    def save(self):
        L = []
        if self.top is not None:
            a = self.top
            while a is not None:
                L.append(a.getdata())
                a = a.get()
        return L[::-1]
