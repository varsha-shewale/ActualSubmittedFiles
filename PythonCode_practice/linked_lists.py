"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

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

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if counter > position:
            #negative position
            return None
        elif counter == position:
            #first position i.e. head
            return current
        elif counter <= position:
            while counter < position-1:
                counter += 1
                current = current.next
            if counter == position-1:
                return current.next
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        print 'insert new_elem %d at position %d' %(new_element.value ,position)
        if counter > position:
            return None

        elif position == 1:
            if current:
                first = current
            self.head = new_element
            if first:
                new_element.next = first

        elif counter < position-1:
            while counter < position-1:
               counter += 1
               current = current.next
               print 'counter: %d, current elem: %d' %(counter, current.value)

            new_element.next = current.next
            current.next = new_element
            print '***********'

        else:
            return None



    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None
        #if linkedlist has atleast 2 elements and
        # element to be deleted is not first i.e. self.head
        while current.value != value and current.next:
            prev = current
            current = current.next

        if current.value == value:
            if prev:
                #if deleting elements starting 2 onwards
                prev.next = current.next
            else:
                #if deleting first element
                self.head = current.next
        return None



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
print ll.get_position(1).value
print ll.get_position(2).value

# Should print 4 now
print ll.get_position(3).value

print ll.get_position(4).value

# Test delete
ll.delete(1)

# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
