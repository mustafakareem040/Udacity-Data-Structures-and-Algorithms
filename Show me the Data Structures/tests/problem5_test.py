import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from datetime import datetime
from problem5 import LinkedList, Block

class TestLinkedList(unittest.TestCase):
    def test_empty_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, 0)

    def test_append_single_block(self):
        linked_list = LinkedList()
        linked_list.append("Block 1")
        self.assertIsInstance(linked_list.head, Block)
        self.assertEqual(linked_list.head.data, "Block 1")
        self.assertEqual(linked_list.head.next, 0)

    def test_append_multiple_blocks(self):
        linked_list = LinkedList()
        linked_list.append("Block 1")
        linked_list.append("Block 2")
        linked_list.append("Block 3")
        self.assertIsInstance(linked_list.head, Block)
        self.assertEqual(linked_list.head.data, "Block 3")
        self.assertIsInstance(linked_list.head.next, Block)
        self.assertEqual(linked_list.head.next.data, "Block 2")
        self.assertIsInstance(linked_list.head.next.next, Block)
        self.assertEqual(linked_list.head.next.next.data, "Block 1")
        self.assertEqual(linked_list.head.next.next.next, 0)

    def test_append_empty_data(self):
        linked_list = LinkedList()
        linked_list.append("")
        self.assertIsInstance(linked_list.head, Block)
        self.assertEqual(linked_list.head.data, "")
        self.assertEqual(linked_list.head.next, 0)

    def test_append_null_data(self):
        linked_list = LinkedList()
        linked_list.append(None)
        self.assertIsInstance(linked_list.head, Block)
        self.assertIsNone(linked_list.head.data)
        self.assertEqual(linked_list.head.next, 0)

    def test_append_large_data(self):
        linked_list = LinkedList()
        large_data =  '世' * 1_000_000  # 1 million characters
        linked_list.append(large_data)
        self.assertIsInstance(linked_list.head, Block)
        self.assertEqual(linked_list.head.data, large_data)
        self.assertEqual(linked_list.head.next, 0)

    def test_append_large_amount_of_values(self):
        linked_list = LinkedList()
        num_values = 1_000_00

        for i in range(num_values):
            linked_list.append(i)

        current_block = linked_list.head
        for i in range(num_values - 1, -1, -1):
            self.assertIsInstance(current_block, Block)
            self.assertEqual(current_block.data, i)
            current_block = current_block.next

        self.assertEqual(current_block, 0)

if __name__ == '__main__':
    unittest.main()
