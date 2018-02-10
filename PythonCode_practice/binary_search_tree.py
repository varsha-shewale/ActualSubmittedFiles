
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

    def bst_helper_insert(self, start, new_val):
        if start:
            if start.value > new_val:
                if start.left is not None:
                    a_node = start.left
                    return self.bst_helper_insert(a_node,new_val)

                elif start.left is None:
                    start.left = Node(new_val)

            elif start.value < new_val:
                if start.right:
                    return self.bst_helper_insert(start.right,new_val)
                elif start.right is None:
                    start.right = Node(new_val)
        return None

    def insert(self, new_val):
        if not self.search(new_val):
            return self.bst_helper_insert(bst.root, new_val)



bst = BinarySearchTree(4)

# Insert elements
bst.insert(2)

bst.insert(1)

bst.insert(3)
bst.insert(5)

print bst.search(3) #returns True
print bst.search(6) #returns False


