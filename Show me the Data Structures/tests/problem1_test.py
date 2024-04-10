import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem1 import Node, LRU_Cache

class TestLRUCache(unittest.TestCase):
    def test_get_and_set(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.set(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.set(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_get_nonexistent_key(self):
        cache = LRU_Cache(2)
        self.assertEqual(cache.get(1), -1)

    def test_set_existing_key(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(1, 2)
        self.assertEqual(cache.get(1), 2)

    def test_set_at_capacity(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_get_with_default_value(self):
        cache = LRU_Cache(2)
        self.assertEqual(cache.get(1, default=-2), -2)

    def test_hash_function(self):
        cache = LRU_Cache(10)
        self.assertEqual(cache._hash(5), 5)
        self.assertEqual(cache._hash(15), 5)
        self.assertEqual(cache._hash('a'), 7)
        self.assertEqual(cache._hash('k'), 7)

    def test_set_with_string_key(self):
        cache = LRU_Cache(2)
        cache.set('ac', 1)
        cache.set('b', 2)
        self.assertEqual(cache.get('ac'), 1)
        self.assertEqual(cache.get('b'), 2)

    def test_get_with_string_key(self):
        cache = LRU_Cache(2)
        cache.set('a', 1)
        cache.set('b', 2)
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('c'), -1)

    def test_set_with_same_hash(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(3, 3)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)
        cache.set(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        cache.set(5, 5)
        cache.set(6, 6)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3, 'random'), 'random')
        self.assertEqual(cache.get(4, 4), 4)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(6), 6)

    def test_get_with_same_hash(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(3, 3)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_set_with_capacity_one(self):
        cache = LRU_Cache(1)
        cache.set(1, 1)
        cache.set(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_get_with_capacity_one(self):
        cache = LRU_Cache(1)
        cache.set(1, 1)
        self.assertEqual(cache.get(1), 1)
        cache.set(2, 2)
        self.assertEqual(cache.get(1), -1)

    def test_get_with_capcity_zero(self):
        cache = LRU_Cache(0)
        cache.set(1, 1)
        self.assertEqual(cache.get(1), -1)
        cache.set(2, 2)
        self.assertEqual(cache.get(2, 'default'), 'default')

    def test_large_input(self):
        cache = LRU_Cache(100000)
        for i in range(100000):
            cache.set(i, i)

        for i in range(100000):
            self.assertEqual(cache.get(i), i)

        cache.set('f', 0)
        self.assertEqual(cache.get(0), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(999), 999)
        self.assertEqual(cache.get(1000), 1000)
        self.assertEqual(cache.get('f'), 0)

if __name__ == '__main__':
    unittest.main()
