def createTreeItem(key, val):
    return key, val

class BST:

    def __init__(self):
        self.key = None
        self.value = None
        self.leftTree = None
        self.rightTree = None

    def isEmpty(self):
        return self.key == None

    def searchTreeInsert(self, key):
        if self.isEmpty():
            self.key = key[0]
            self.value = key[1]
            return True
        else:
            if key[0] < self.key:
                if self.leftTree == None:
                    left = BST()
                    left.key = key[0]
                    left.value = key[1]
                    self.leftTree = left
                    return True
                else:
                    self.leftTree.searchTreeInsert(key)
                    return True
            elif key[0] > self.key:
                if self.rightTree == None:
                    right = BST()
                    right.key = key[0]
                    right.value = key[1]
                    self.rightTree = right
                    return True
                else:
                    self.rightTree.searchTreeInsert(key)
                    return True
        return False

    def searchTreeRetrieve(self, keyType):

        if self.isEmpty():
            return self.key, False
        elif self.key == keyType:
            return self.key, True
        elif keyType < self.key:
            if self.leftTree == None:
                return None, False
            elif self.leftTree.key == keyType:
                return self.leftTree.key, True
            else:
                return self.leftTree.searchTreeRetrieve(keyType)
        elif keyType > self.key:
            if self.rightTree == None:
                return None, False
            elif self.rightTree.key == keyType:
                return self.rightTree.key, True
            else:
                return self.rightTree.searchTreeRetrieve(keyType)

    def inorderTraverse(self, print):

        if not self.isEmpty():

            if self.leftTree != None:
                self.leftTree.inorderTraverse(print)

            print(self.key)

            if self.rightTree != None:
                self.rightTree.inorderTraverse(print)

    def postorderTraverse(self, print):

        if not self.isEmpty():

            if self.leftTree != None:
                self.leftTree.postorderTraverse(print)

            if self.rightTree != None:
                self.rightTree.postorderTraverse(print)

            print(self.key)

    def inorderLeeg(self):

        if not self.isEmpty():

            if self.leftTree != None:
                self.leftTree.inorderLeeg()

            self.leftTree = None
            self.rightTree = None
            self.key = None

            if self.rightTree != None:
                self.rightTree.inorderLeeg()

    def load(self, boom):


        if not self.isEmpty():
            self.inorderLeeg()
        self.key = None



        def boomlezen(tree):

            if tree != None:  # elke dict binnen de dict mag niet leeg zijn

                if tree['root'] != None:  # als de boom geen blad is
                    key = createTreeItem(tree['root'], tree['root'])
                    self.searchTreeInsert(key)  # de root eerst inserten in de BST

                if tree.get('children') != None:
                    boomlezen(tree['children'][
                                  0])  # en telkens hetzelfde met de twee siblings (eerst linker en dan rechter) --> recursie
                    boomlezen(tree['children'][1])

        boomlezen(boom)

    def loadsave(self, geen_Left_Right):


        if self.leftTree is not None:
            left = self.leftTree.loadsave(False)
        else:
            left = None

        if self.rightTree is not None:
            right = self.rightTree.loadsave(False)
        else:
            right = None

        savedTree = {'root': self.key}

        if self.leftTree is None and self.rightTree is None:
            geen_Left_Right = True
        if self.leftTree is None and self.rightTree is None:
            geen_Left_Right = True

        if not geen_Left_Right:
            savedTree.update({'children': [left, right]})

        return savedTree

    def save(self):
        if self.key != None:
            return self.loadsave(False)

        '''
        eerst had ik het zoals c++ gemaakt en ik had het helemaal vergeten dat je een dictionary (of een databank/conatainer) kan printen in python

        string = "{"

        if self.isEmpty():
            string += "'root': " + None + "]"
        else:
            string += "'root': " + str(self.key)
            if self.leftTree != None:
                string += ",'children':[" + str(self.leftTree.save())
            if self.rightTree != None:
                string += str(self.rightTree.save())
                string += "]"

        string += "}"

        return string
        '''

    def searchTreeDelete(self, data):
        """

        :param data: de key die verwijdert moet worden uit de boom
        :return: true als de key in de boom verwijdert kan worden
        """
        # lege boom
        if self.key == None:
            return False

        # Geval 1: data zit in de key
        elif self.key == data:
            if self.leftTree == None and self.rightTree == None:  # key is een blad
                self.key = None
            elif self.leftTree and self.rightTree == None:  # geen righttree
                self.key = self.leftTree.key
                self.leftTree.searchTreeDelete(self.leftTree.key)
            elif self.leftTree == None and self.rightTree:  # geen lefttree
                self.key = self.rightTree.key
                self.rightTree.searchTreeDelete(self.rightTree.key)
            elif self.leftTree and self.rightTree:  # key heeft left- en righttree -> inorder successor
                deleteNodeRoot = self
                deleteNode = self.rightTree
                while deleteNode.leftTree:
                    deleteNodeRoot = deleteNode
                    deleteNode = deleteNode.leftTree

                self.key = deleteNode.key
                if deleteNode.rightTree:  # rechtertree van deleteNode koppelen aan de root van deleteNode
                    if deleteNodeRoot.key > deleteNode.key:
                        deleteNodeRoot.leftTree = deleteNode.rightTree
                    elif deleteNodeRoot.key < deleteNode.key:
                        deleteNodeRoot.rightTree = deleteNode.rightTree
                else:  # anders deleteNode gewoon loskoppelen en None maken
                    if deleteNode.key < deleteNodeRoot.key:
                        deleteNodeRoot.leftTree = None
                    else:
                        deleteNodeRoot.rightTree = None

            return True

        root = None
        node = self

        # zoeken naar de te-verwijderen key

        while node and node.key != data:
            root = node
            if data < node.key:
                node = node.leftTree
            elif data > node.key:
                node = node.rightTree

        # Geval 2: data zit niet in de boom

        if node is None or node.key != data:
            return False

        # Geval 3: de te-verwijderen key heeft geen left- of rightTree

        elif node.leftTree is None and node.rightTree is None:
            if data < root.key:
                root.leftTree = None
            else:
                root.rightTree = None
            return True

        # Geval 4: alleen left tree bestaat van het te-verwijderen key

        elif node.leftTree and node.rightTree is None:
            if data < root.key:
                root.leftTree = node.leftTree
            else:
                root.rightTree = node.leftTree
            return True

        # Geval 4: alleen right tree bestaat van het te-verwijderen key

        elif node.leftTree and node.rightTree is None:
            if data < root.key:
                root.leftTree = node.rightTree
            else:
                root.rightTree = node.rightTree
            return True

        # Geval 4: right en left tree bestaan

        else:
            deleteNodeRoot = node
            deleteNode = node.rightTree
            while deleteNode.leftTree:
                deleteNodeRoot = deleteNode
                deleteNode = deleteNode.leftTree

            node.key = deleteNode.key
            if deleteNode.rightTree:
                if deleteNodeRoot.key >= deleteNode.key:
                    deleteNodeRoot.leftTree = deleteNode.rightTree
                elif deleteNodeRoot.key <= deleteNode.key:
                    deleteNodeRoot.rightTree = deleteNode.rightTree
            else:
                if deleteNode.key <= deleteNodeRoot.key:
                    deleteNodeRoot.leftTree = None
                else:
                    deleteNodeRoot.rightTree = None