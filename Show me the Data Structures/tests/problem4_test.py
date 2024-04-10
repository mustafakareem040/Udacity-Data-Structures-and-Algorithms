import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem4 import Group, is_user_in_group
import unittest

class TestIsUserInGroup(unittest.TestCase):
    def setUp(self):
        self.parent_group = Group("Parent")
        self.child_group1 = Group("Child1")
        self.child_group2 = Group("Child2")
        self.grandchild_group = Group("Grandchild")
        self.grandchild_group2 = Group("Grandchild")
        self.parent_group.add_group(self.child_group1)
        self.parent_group.add_group(self.child_group2)
        self.child_group1.add_group(self.grandchild_group)
        self.grandchild_group.add_group(self.grandchild_group2)

    def test_user_in_parent_group(self):
        self.parent_group.add_user("user1")
        self.assertTrue(is_user_in_group("user1", self.parent_group))

    def test_user_in_child_group(self):
        self.child_group1.add_user("user2")
        self.assertTrue(is_user_in_group("user2", self.parent_group))

    def test_user_in_grandchild_group(self):
        self.grandchild_group.add_user("user3")
        self.assertTrue(is_user_in_group("user3", self.parent_group))

    def test_user_not_in_group(self):
        self.assertFalse(is_user_in_group("user4", self.parent_group))

    def test_user_in_multiple_groups(self):
        self.parent_group.add_user("user5")
        self.child_group2.add_user("user5")
        self.assertTrue(is_user_in_group("user5", self.parent_group))

    def test_empty_group(self):
        empty_group = Group("")
        self.assertFalse(is_user_in_group("user6", empty_group))
        empty_group.add_user('user6')
        self.assertTrue(is_user_in_group("user6", empty_group))

  

if __name__ == '__main__':
    unittest.main()
