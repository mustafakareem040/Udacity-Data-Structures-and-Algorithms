import sys
from heapq import heapify, heappush, heappop
from functools import total_ordering
from collections import Counter

@total_ordering
class Node:
    def __init__(self, char, count=1, left=None, right=None):
        self.char = char
        self.count = count
        self.left = left
        self.right =  right

    def has_child(self):
        return bool(self.left or self.right)

    def __gt__(self, other):
        return self.count > other.count if isinstance(other, Node) else other

    def __eq__(self, other):
        return self.count == other.count if isinstance(other, Node) else other

    def __add__(self, other):
        if isinstance(other, int):
            return self.count + other
        return self.count + other.count

    def __repr__(self):
        if self.char is None:
            return repr(self.count)
        return repr(f'{self.count}{self.char}')




def dfs(root, arr, table):
    if not root:
        return
    if not root.has_child():
        table[root.char] = arr
        return
    dfs(root.left, arr+'0', table)
    dfs(root.right, arr+'1', table)
    return table

def huffman_encoding(data):
    counter = Counter(data)
    nodes = []
    heapify(nodes)
    while counter:
        node = Node(*counter.popitem())
        heappush(nodes, node)
    root = None
    if len(nodes) == 0:
        return "", None
    if len(nodes) == 1:
        n = heappop(nodes)
        root = Node(None, n.count, Node(n.char, n.count))
    while len(nodes) > 1:
        left = heappop(nodes)
        right = heappop(nodes)
        s = right+left
        root = Node(None, s, left, right)
        heappush(nodes, root)
    if nodes:
        root = Node(None, heappop(nodes), root.left, root.right)
    table = dfs(root, '', {})
    encoded = ""
    for i in data:
        encoded += table[i]
    return encoded, root

def huffman_decoding(data, tree):
    if data == "":
        return ""
    result = ""
    node = tree
    for i in data:
        if not node.has_child():
            result += node.char
            node = tree
        if i == '0':
            node = node.left
        else:
            node = node.right
    if not node.has_child():
            result += node.char
            node = tree
    return result


