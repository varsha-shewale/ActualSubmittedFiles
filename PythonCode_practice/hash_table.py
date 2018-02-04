
class HashTable(object):
    def __init__(self):
        #creates a table of 10000 lists with None values
        self.table = [None]*10000

    def calculate_hash_value(self,string):
        hv = ord(string[0])*100 + ord(string[1])
        if hv != -1:
            return hv
        return -1

    def store(self,string):
        """Input a string that's stored in
        the table."""
        hv = self.calculate_hash_value(string)
        if self.table[hv] != None:
            self.table[hv].append(string)
        else:
            self.table[hv] = [string]

        #print self.table[hv]
        return None

    def lookup(self,string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None: #this check is important to if string is in self.table
                if string in self.table[hv]:
                    return hv
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')


# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
