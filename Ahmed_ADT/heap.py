class Node:
    def __init__(self,value,parent=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
class Heap:
    def __init__(self,maxHeap=True):
        self.root = None
        self.maxHeap = maxHeap

    def heapIsEmpty(self):
        # Als er geen root is ,  leeg
        if self.root is None:
            return True
        return False

    def minMax(self, newNode):
        # zorgt voor implementatie minheap/MAXHEAP aan de hand van de waarde van de bool maxHeap.
        if self.maxHeap:
            # if True, verwisselen we de Nodes zodat de waarde van elke node groter is dan die van zijn kinderen. While loop zodat we blijven verwisselen tot we een maxheap krijgen
            while (newNode.parent is not None) and (newNode.value > newNode.parent.value):
                newNode.value, newNode.parent.value = newNode.parent.value, newNode.value
                newNode = newNode.parent
        if not self.maxHeap:
            # geval waarbij minheap: nodes verwisselen zodat, de waarde van elke node kleiner is dan die van zijn kinderen. While loop zodat we blijven verwisselen tot we een minheap krijgen
            while (newNode.parent is not None) and (newNode.value < newNode.parent.value):
                newNode.value, newNode.parent.value = newNode.parent.value, newNode.value
                newNode = newNode.parent

    def heapInsert(self, value):
        new_node = Node(value)
        if self.heapIsEmpty():
            self.root = new_node
            return True
        else:
            current = self.root
            while True:
                if current.left is None:
                    current.left = new_node
                    current.left.parent = current
                    if self.heapIsEmpty() != True:
                      self.minMax(new_node)
                    return True
                elif current.right is None:
                    current.right = new_node
                    current.right.parent = current
                    if self.heapIsEmpty() != True:
                      self.minMax(new_node)
                    return True
                elif (current.left.left is not None and current.left.right is not None) and (current.right.left is None or current.right.right is None):
                    current = current.right
                else:
                    current = current.left


    def lastNodeGetter(self):
        lijst = [self.root]
        for i in lijst:
            if i.left: lijst.append(i.left)
            if i.right: lijst.append(i.right)
        return i

    def heapifyDown(self, node):
        # sorteert de heap correct voor max/min heaps
        left_child = node.left
        right_child = node.right
        if self.maxHeap:
            if left_child is not None and left_child.value > node.value and (right_child is None or left_child.value > right_child.value):
                node.value, left_child.value = left_child.value, node.value
                self.heapifyDown(left_child)
            elif right_child is not None and right_child.value > node.value:
                node.value, right_child.value = right_child.value, node.value
                self.heapifyDown(right_child)
        else:
            if left_child is not None and left_child.value < node.value and (right_child is None or left_child.value < right_child.value):
                node.value, left_child.value = left_child.value, node.value
                self.heapifyDown(left_child)
            elif right_child is not None and right_child.value < node.value:
                node.value, right_child.value = right_child.value, node.value
                self.heapifyDown(right_child)

    def heapDelete(self):
        # als leeg, kunnen we niets verwijderen
        if self.heapIsEmpty():
            return None, False
        # root deleten en verplaatsen met last Node value
        lastNode = self.lastNodeGetter()
        deleted = self.root.value
        self.root.value = lastNode.value

        if lastNode.parent.left == lastNode:
            lastNode.parent.left = None
        else:
            lastNode.parent.right = None
        self.heapifyDown(self.root)
        # omdat we root hebben veranderd, klopt de min/max heap niet meer en moeten we heapifyen om de balans terug correct te krijgen.
        return deleted, True



    def save(self, node=None):
        # heap als dict
        if node is None:
            node = self.root
        if node:
            tree = {'root': node.value}
            if node.left is not None or node.right is not None:
                tree['children'] = []
                if node.left is not None:
                    tree['children'].append(self.save(node.left))
                else:
                    tree['children'].append(None)
                if node.right is not None:
                    tree['children'].append(self.save(node.right))
                else:
                    tree['children'].append(None)
        return tree

    def buildTree(self, node, children):
        if children:
            left_child, right_child = children
            if left_child:
                node.left = Node(left_child['root'])
                node.left.parent = node
                self.buildTree(node.left, left_child.get('children'))
            if right_child:
                node.right = Node(right_child['root'])
                node.right.parent = node
                self.buildTree(node.right, right_child.get('children'))

    def load(self, data):
        self.root = Node(data['root'])
        self.buildTree(self.root, data.get('children'))