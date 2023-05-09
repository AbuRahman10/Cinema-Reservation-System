def createTreeItem(key, value):
    item = BST()
    item.key = key
    item.value = value
    return (key, value)


class BST:
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None

    def isEmpty(self):
        if self.key is None:
            return True
        return False

    def save(self, noChildren=False):
        if self.left is not None:
            left = self.left.save(False)
        else:
            left = None
        if self.right is not None:
            right = self.right.save(False)
        else:
            right = None

        tree = {'root': self.key}

        if self.left is None and self.right is None:
            noChildren = True
        if self.left is None and self.right is None:
            noChildren = True

        if not noChildren and tree['root'] is not None:
            tree.update({'children': [left, right]})

        return self.corrected(tree)

    def corrected(self, tree):
        if len(tree) == 2:
            if tree['children'][0]:
                if tree['children'][0]['root'] is None:
                    tree['children'][0] = None
                else:
                    self.corrected(tree['children'][0])

            if tree['children'][1]:
                if tree['children'][1]['root'] is None:
                    tree['children'][1] = None
                else:
                    self.corrected(tree['children'][1])

        return self.delete_children(tree)

    def delete_children(self, tree):
        if len(tree) == 2:
            if tree['children'][0] is None and tree['children'][1] is None:
                tree.pop('children', None)
            else:
                if tree['children'][0]:
                    self.delete_children(tree['children'][0])

                if tree['children'][1]:
                    self.delete_children(tree['children'][1])
        return tree

    def load(self, tree):
        if not self.isEmpty():
            self.emptyTree()
        self.key = None

        def recursionTreeDict(boom):

            if boom is not None:
                if boom['root'] is not None:
                    newNode = createTreeItem(boom['root'], boom['root'])
                    self.searchTreeInsert(newNode)

                if boom.get('children') is not None:
                    recursionTreeDict(boom['children'][0])
                    recursionTreeDict(boom['children'][1])

        recursionTreeDict(tree)

    def emptyTree(self):
        if self.key:
            if self.left is not None:
                self.left.emptyTree()
            if self.right is not None:
                self.right.emptyTree()

        self.left = None
        self.right = None
        self.key = None

    def searchTreeInsert(self, key):
        """

        :param key: de slot die in de boom opgeslagen wordt
        :return: true als key in de boom geplaatst kan worden
        """

        if self.isEmpty():
            self.key = key[0]
            self.value = key[1]
            return True
        else:
            if key[0] < self.key:
                if self.left == None:
                    left = BST()
                    left.key = key[0]
                    left.value = key[1]
                    self.left = left
                    return True
                else:
                    self.left.searchTreeInsert(key)
                    return True
            elif key[0] > self.key:
                if self.right == None:
                    right = BST()
                    right.key = key[0]
                    right.value = key[1]
                    self.right = right
                    return True
                else:
                    self.right.searchTreeInsert(key)
                    return True
        return False


    def searchTreeRetrieve(self, keyType):

        if self.isEmpty():
            return self.key, False
        elif self.key == keyType:
            return self.key, True
        elif keyType < self.key:
            if self.left is None:
                return None, False
            elif self.left.key == keyType:
                return self.left.key, True
            else:
                return self.left.searchTreeRetrieve(keyType)
        elif keyType > self.key:
            if self.right is None:
                return None, False
            elif self.right.key == keyType:
                return self.right.key, True
            else:
                return self.right.searchTreeRetrieve(keyType)

    def inorderTraverse(self, print):
        self.inorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key)
        if self.right is not None:
            self.right.inorder()

    def searchTreeDelete(self, key):
        if self.isEmpty():
            return False
        return self.delete(key)

    def delete(self, key):
        if not self.searchTreeRetrieve(key):
            return False
        else:
            if key == self.key:
                # delete leaf
                if self.left is None and self.right is None:
                    self.key = None
                    return True
                # delete node with 1 child
                elif self.left is None and self.right is not None:
                    if self.right.right is None and self.right.left is None:
                        self.key = self.right.minValue()
                        return True
                    else:
                        self.inorderSuccessor()
                        return True
                elif self.left is not None and self.right is None:
                    if self.left.right is None and self.left.left is None:
                        self.key = self.left.minValue()
                        return True
                    else:
                        self.inorderSuccessor()
                        return True
                # delete node with 2 child
                elif self.left is not None and self.right is not None:
                    self.inorderSuccessor()
                    return True
            elif key < self.key:
                return self.left.delete(key)
            else:
                return self.right.delete(key)

    def inorderSuccessor(self):
        if self.right is not None and self.left is None:
            if self.right.left is None:
                self.key = self.right.minValue()
            else:
                self.key = self.right.left.minValue()
        elif self.right is None and self.left is not None:
            if self.left.left is None:
                self.key = self.left.minValue()
            else:
                self.key = self.left.left.minValue()
        elif self.right is not None and self.left is not None:
            if self.right.left is None:
                self.key = self.right.minValue()
            else:
                self.key = self.right.left.minValue()

    def minValue(self):
        if self.left is not None:
            self.left.minValue()
        output = self.key
        self.key = None
        return output
