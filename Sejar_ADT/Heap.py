class Heap:
    def __init__(self, maxHeap=True, key=None):
        self.parent = None
        self.left = None
        self.right = None
        self.type = maxHeap
        self.key = key
        self.count = 0
        self.data = None

    def heapIsEmpty(self):
        return self.key is None

    def Last_element(self):
        path = bin(self.count)
        path = str(path)
        path = path[3:]

        if self.count == 1:
            return self

        temp = self
        for i in path:
            if i == '1':
                temp = temp.right
            elif i == '0':
                temp = temp.left

        return temp

    def Last_parent(self):
        path = bin(self.count)
        path = str(path)
        path = path[3:]
        path = path[:-1]

        if self.count == 1:
            return self
        elif self.count == 2:
            return self
        elif self.count == 3:
            return self

        temp = self
        for i in path:
            if i == '1':
                temp = temp.right
            elif i == '0':
                temp = temp.left

        return temp

    def findNextInsert(self):
        path = bin(self.count + 1)
        path = str(path)
        path = path[3:]
        path = path[:-1]

        if self.count < 3:
            return self

        else:
            temp = self
            for i in path:
                if i == '1':
                    temp = temp.right
                elif i == '0':
                    temp = temp.left
        return temp

    def up(self):
        while self.parent.key < self.key:
            temp = self.key
            self.key = self.parent.key
            self.parent.key = temp
            if self.parent.parent is not None:
                self = self.parent

    def down(self):
        if (self.left is not None) and (self.right is not None):
            temp1 = self.key - self.left.key
            temp2 = self.key - self.right.key
            if (temp1 > 0) and (temp2 > 0):
                return
            elif (temp1 < 0) and (temp2 > 0):
                temp = self.left.key
                self.left.key = self.key
                self.key = temp
                self.left.down()
            elif (temp1 > 0) and (temp2 < 0):
                temp = self.right.key
                self.right.key = self.key
                self.key = temp
                self.left.down()

            elif (temp1 < 0) and (temp2 < 0):
                if temp1 < temp2:
                    temp = self.left.key
                    self.left.key = self.key
                    self.key = temp
                    self.left.down()

                else:
                    temp = self.right.key
                    self.right.key = self.key
                    self.key = temp
                    self.left.down()

        if (self.left is not None) and (self.right is None):
            if self.left.key > self.key:
                temp = self.key
                self.key = self.left.key
                self.left.key = temp
                return
            return

        if self.left is None:
            return

    def heapDelete(self):
        if self.heapIsEmpty():
            return None, False

        else:
            temp = self.key
            self.key = self.Last_element().key
            if self.Last_parent().right is not None:
                self.Last_parent().right = None
                self.count -= 1
            else:
                self.Last_parent().left = None
                self.count -= 1

        self.down()
        return temp, True

    def root(self):
        if self.parent is None:
            return self
        if self.parent is not None:
            return self.parent.root()

    def heapInsert(self, data):
        if self.key is None:
            self.key = data[0]
            self.data = data[1]
            self.root().count += 1
            return True
        else:
            newItem = Heap(True, data)
            if self.findNextInsert().left is None:
                self.findNextInsert().left = newItem
                self.root().count += 1
                self.Last_element().parent = self.Last_parent()
            else:
                self.findNextInsert().right = newItem
                self.root().count += 1
                self.Last_element().parent = self.Last_parent()

        self.Last_element().up()
        return True


    def save(self):
        if self.key is None:
            return {}
        save = {'root': self.data}
        if (self.right is not None) and (self.left is not None):
            save['children'] = [self.left.save(), self.right.save()]
        elif (self.right is not None) and (self.left is None):
            save['children'] = [None, self.right.save()]
        elif (self.right is None) and (self.left is not None):
            save['children'] = [self.left.save(), None]
        return save

    def load(self, dict):
        self.key = Heap(self.type, None).key
        self.left = None
        self.right = None
        self.count = 0
        self.heapInsert(dict['root'])
        if 'children' in dict:
            if dict['children'][0] is not None:
                self.left = Heap(self.type, None)
                self.left.parent = self
                self.left.load(dict['children'][0])
            if dict['children'][1] is not None:
                self.right = Heap(self.type, None)
                self.right.parent = self
                self.right.load(dict['children'][1])