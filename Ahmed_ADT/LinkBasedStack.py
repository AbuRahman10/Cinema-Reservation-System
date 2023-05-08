class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def getTop(self):
        if self.isEmpty():
            return None,False
        else:
            return self.top.data,True

    def push(self, value):
        node = Node(value)
        if (self.top == None):
            self.top = node
        else:
            node.next = self.top
            self.top = node
        return True

    def pop(self):
        if self.isEmpty():
            return None, False
        popped = self.top.data
        self.top = self.top.next
        return popped, True


    def save(self):
        stack = []
        current = self.top
        while current is not None:
            stack.append(current.data)
            current = current.next
        return stack[::-1]

    def load(self, data):
        self.top = None
        for i in range(len(data)):
            self.push(data[i])
        return self.top,True