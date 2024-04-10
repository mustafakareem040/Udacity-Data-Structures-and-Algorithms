class Node:
    def __init__(self, key, item, next_bucket=None, next_node=None, previous=None, index=None):
        self.key = key
        self.item = item
        self.next = next_node
        self.next_bucket = next_bucket
        self.previous = previous
        self.index = index


class Pipe(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def _append(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
    
    def append(self, key, item): # I realized this is useless later but I'll keep it.
        if not self.head:
            self.head = Node(key, item)
            self.tail = self.head
            return
        node = Node(key, item, next_node=self.head)
        self.head.previous = node
        self.head = node

    def pop(self):
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return node

    def set_first(self, node):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = node.previous # Remove from tail
        else:
            node.next.previous = node.previous # Remove the next previous link
        node.previous.next = node.next # Remove the previous next link
        node.previous = None # head has no previous
        node.next = self.head # Setting current head to be next value
        self.head.previous = node # Setting head previous to new head
        self.head = node # I am done
        



    def pop_last(self):
        if self.head  == self.tail: # Including if list is empty
            self.head = None
            self.tail = None
        else:
            previous = self.tail.previous
            self.tail = previous
            if previous:
                previous.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.arr = [None for _ in range(capacity)]
        self.capacity = capacity if capacity else -1 # For handling capacity of 0
        self.length = 0
        self.sequence = Pipe()


    def get(self, key, default=-1):
        # Retrieve item from provided key. Return default if nonexistent. 
        if self.length == 0:
            return default
        index = self._hash(key)
        node = self.arr[index]
        while node:
            if node.key == key:
                self.sequence.set_first(node)
                return node.item
            node = node.next
        return default # return default instead of constant value


    def set(self, key, item):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == -1:
            return
        index = self._hash(key)
        node = self.arr[index]
        while node:
            if node.key == key:
                node.item = item
                self.sequence.set_first(node)
                return
            node = node.next_bucket
        if self.length >= self.capacity:
            k = self.sequence.tail
            self._pop(k.key, k.index)
            self.sequence.pop_last()
            self.length -= 1
        new = Node(key, item, next_bucket=self.arr[index], index=index)
        self.arr[index] = new
        self.sequence._append(new)
        self.length += 1

    def _pop(self, key, index):
        node = self.arr[index]
        if node and node.key == key:
            self.arr[index] = self.arr[index].next_bucket
        else:
            while node.next_bucket:
                if node.next_bucket.key == key:
                    node.next_bucket = node.next_bucket.next_bucket # NEXT NEXT NEXT
                    break


    def _hash(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return ord(str(key)[0]) % self.capacity



