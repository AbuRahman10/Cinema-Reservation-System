from Sejar_ADT.BST import BST

class BSTTable:
    def __init__(self):
        self.bst = BST()

    def tableIsEmpty(self):
        return self.bst.isEmpty()

    def tableInsert(self, value):
        return self.bst.searchTreeInsert(value)

    def tableDelete(self, key):
        return self.bst.searchTreeDelete(key)

    def tableRetrieve(self, key):
        return self.bst.searchTreeRetrieve(key)

    def traverseTable(self, key = None):
        return self.bst.inorderTraverse(key)

    def save(self):
        return self.bst.save()

    def load(self, a):
        self.bst.load(a)