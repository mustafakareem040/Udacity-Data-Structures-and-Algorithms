import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash, next_node=None):
      self.timestamp = timestamp
      self.data = data
      self.next = next_node
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(str(timestamp)) # Since it is a synchronous operation it is impossible to implement two hashes at the same time

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class LinkedList:
      def __init__(self):
            self.head = 0

      def append(self, data):
            self.head = Block(datetime.utcnow(), data, self.head and self.head.hash, self.head)

