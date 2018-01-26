"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        #insert_first is efficient than append bcoz
        # in append one has to go through the whole LL to append at end.

        "Insert new element as the head of the LinkedList"
        #store current self.head
        current = self.head

        #assign self.head to new_elment
        self.head = new_element

        #assign stored self.head to new_element's next
        new_element.next = current
        return None

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            #get current first element
            current = self.head

            #get current's next
            new_head = current.next

            #assign current's next to self.head (i.e. 2nd element now becomes head of LL)
            self.head = new_head

            #clear current first element's 'next' reference address
            #print current.value

            current.next = None
            #print current.value
            #print current.next
            return current
        else:
            #print 'Stack is empty, no element to delete!'
            return None

class Stack(object):
    def __init__(self,top=None):
        try:
            self.ll = LinkedList(top)
        except:
            print 'Linked list creation failed'

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        return self.ll.insert_first(new_element)


    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value