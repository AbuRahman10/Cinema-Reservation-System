class Node:
    def __init__(self, key, value,left=None,right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right

def createTreeItem(key, value):
    return Node(key,value)

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def searchTreeInsert(self, newNode):
        parent = self.root
        if not parent:
            self.root = newNode
            return True
        while parent:
            if parent.key > newNode.key:
                if not parent.left:
                    parent.left = newNode
                    return True
                parent = parent.left
            elif parent.key < newNode.key:
                if not parent.right:
                    parent.right = newNode
                    return True
                parent = parent.right
            else:
                parent.val = newNode.val
                return True

    def searchTreeRetrieve(self, key):
        parent = self.root
        if not parent: return (None, False)
        while parent:
            if parent.key == key:
                return (parent.value, True)
            elif parent.key > key:
                parent = parent.left or (None, False)
            else:
                parent = parent.right or (None, False)
        return (None, False)

    def inorderTraverse(self, x):
        if self.root:
            self.inorder(self.root)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    def save(self):
        output = {'root': self.root.value}
        if self.root.left or self.root.right:
            output['children'] = [None, None]
        if self.root.left:
            output['children'][0] = self.dictt(self.root.left)
        if self.root.right:
            output['children'][1] = self.dictt(self.root.right)
        return output
    def dictt(self, root):
        if root is None:
            return None
        output = {'root': root.value}
        if root.left or root.right:
            output['children'] = [None, None]
        if root.left:
            output['children'][0] = self.dictt(root.left)
        if root.right:
            output['children'][1] = self.dictt(root.right)
        return output

    def load(self, data):
        self.root = Node(data['root'], data['root'])
        self.list(self.root, data.get('children'))

    def list(self, node, children):
        if children:
            l, r = children
            node.left = Node(l['root'], l['root']) if l else None
            self.list(node.left, l.get('children')) if l else None
            node.right = Node(r['root'], r['root']) if r else None
            self.list(node.right, r.get('children')) if r else None

    def searchTreeDelete(self, key):
        if self.root is None:
            return False
        else:
            # Zoeken naar de to be deleted node
            parent = None
            to_del = self.root
            while to_del and to_del.key != key:
                parent = to_del
                if key < to_del.key:
                    to_del = to_del.left
                else:
                    to_del = to_del.right
                if to_del is None:
                    return False
            # de te verwijderen node is een leaf, en de childeren zijn dus None
            if to_del.left is None and to_del.right is None:
                if parent is None:
                    self.root = None
                elif parent.left == to_del:
                    parent.left = None
                else:
                    parent.right = None
            # de te verwijderen Node heeft 1  child
            elif to_del.left is None or to_del.right is None:
                if to_del.left:
                    child = to_del.left
                else:
                    child = to_del.right
                if parent is None:
                    self.root = child
                elif parent.left == to_del:
                    parent.left = child
                else:
                    parent.right = child
            # de te delete node heeft 2 childs
            else:
                parent_of_successor = to_del
                successor = to_del.right
                while successor.left:
                    parent_of_successor = successor
                    successor = successor.left
                to_del.key = successor.key
                to_del.value = successor.value
                if parent_of_successor.left == successor:
                    parent_of_successor.left = None
                else:
                    parent_of_successor.right = None
            return True