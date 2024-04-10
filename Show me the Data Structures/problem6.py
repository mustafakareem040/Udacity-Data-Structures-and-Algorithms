from collections import Counter
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return ""
        cur_head = self.head
        out_string = ""
        while cur_head.next:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        else:
            out_string += str(cur_head.value)
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

def union(llist_1, llist_2) -> LinkedList:
    # Your Solution Here
    result = LinkedList()
    result.head = Node(None) # Dummy node
    node = result.head
    for i in llist_1: # Assuming duplications are allowed
        node.next = Node(i.value) # For optimizations I didn't use append method
        node = node.next
    for i in llist_2:
        node.next = Node(i.value)
        node = node.next
    result.head = result.head.next # Deleting the dummy node 
    return result


def intersection(llist_1, llist_2):

    result = LinkedList()
    result.head = Node(None)
    node = result.head
    counter = dict()
    for i in llist_1:
        val = i.value
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for i in llist_2:
        val = i.value
        if counter.get(val):
            counter[val] -= 1
            node.next = Node(val)
            node = node.next
    result.head = result.head.next
    return result



