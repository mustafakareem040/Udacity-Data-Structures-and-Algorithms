import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem6 import LinkedList, union, intersection
class TestLinkedListOperations(unittest.TestCase):
    def setUp(self):
        self.empty_list = LinkedList()
        
        self.list1 = LinkedList()
        self.list1.append(1)
        self.list1.append(2)
        self.list1.append(3)
        self.list1.append(2)
        
        self.list2 = LinkedList()
        self.list2.append(2)
        self.list2.append(4)
        self.list2.append(6)
        self.list2.append(2)
        
        self.list3 = LinkedList()
        self.list3.append(1)
        self.list3.append(2)
        self.list3.append(3)
    
    def test_union(self):
        # Test case 1: Union of two non-empty linked lists
        result = union(self.list1, self.list2)
        expected = "1 -> 2 -> 3 -> 2 -> 2 -> 4 -> 6 -> 2"
        self.assertEqual(str(result), expected)
        
        # Test case 2: Union of an empty linked list and a non-empty linked list
        result = union(self.empty_list, self.list1)
        expected = "1 -> 2 -> 3 -> 2"
        self.assertEqual(str(result), expected)
        
        # Test case 3: Union of a non-empty linked list and an empty linked list
        result = union(self.list2, self.empty_list)
        expected = "2 -> 4 -> 6 -> 2"
        self.assertEqual(str(result), expected)
        
        # Test case 4: Union of two empty linked lists
        result = union(self.empty_list, self.empty_list)
        expected = ""
        self.assertEqual(str(result), expected)
        
    
    def test_intersection(self):
        # Test case 1: Intersection of two non-empty linked lists with duplicates
        result = intersection(self.list1, self.list2)
        expected = "2 -> 2"
        self.assertEqual(str(result), expected)
        
        # Test case 2: Intersection of two non-empty linked lists without duplicates
        result = intersection(self.list1, self.list3)
        expected = "1 -> 2 -> 3"
        self.assertEqual(str(result), expected)
        
        # Test case 3: Intersection of an empty linked list and a non-empty linked list
        result = intersection(self.empty_list, self.list1)
        expected = ""
        self.assertEqual(str(result), expected)
        
        # Test case 4: Intersection of a non-empty linked list and an empty linked list
        result = intersection(self.list2, self.empty_list)
        expected = ""
        self.assertEqual(str(result), expected)
        
        # Test case 5: Intersection of two empty linked lists
        result = intersection(self.empty_list, self.empty_list)
        expected = ""
        self.assertEqual(str(result), expected)

if __name__ == '__main__':
    unittest.main()