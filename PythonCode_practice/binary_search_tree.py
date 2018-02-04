
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self, root_val):
       self.root = Node(root_val)

    def bst_helper_search(self,start,find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                return self.bst_helper_search(start.left, find_val)
            elif start.value < find_val:
                return self.bst_helper_search(start.right,find_val)
        return False

    def search(self,find_val):
        return self.bst_helper_search(bst.root, find_val)

bst = BinarySearchTree(4)
bst.root.left = Node(2)
bst.root.right = Node(5)
bst.root.left.left = Node(1)
bst.root.left.right = Node(3)

print bst.search(3) #returns True
print bst.search(6) #returns FAlse

