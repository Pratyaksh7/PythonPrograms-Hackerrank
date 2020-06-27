"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
        
    def store(self , string):
        val = self.calculate_hash_value(string)
        if val != -1:
            if self.table[val] != None:
                self.table[val].append(string)
            else:
                self.table[val] = [string]
        
        
    def lookup(self , string):
        val = self.calculate_hash_value(string)
        if val != -1:
            if self.table[val] != None:
                if string in self.table[val]:
                    return val
        return -1
        
    def calculate_hash_value(self, string): 
        """Helper function to calulate a
        hash value from a string."""
        value = ord(string[0])*100 + ord(string[1])
        return value
        
        
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print( hash_table.lookup('UDACIOUS'))
    