"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in 
        the table."""
        k = self.calculate_hash_value(string)
        t = self.table[k]
        if t:
            t.append(string)
        else:
            self.table[k] = [string]

    def lookup(self, string):
        """TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        k = self.calculate_hash_value(string)
        t = self.table[k]
        if t:
            for i in t:
                if i == string:
                    return k
                
        return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])

