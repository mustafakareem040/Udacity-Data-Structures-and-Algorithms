import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem3 import Node, huffman_encoding, huffman_decoding
import sys

class TestHuffmanCoding(unittest.TestCase):
    def test_single_character(self):
        data = "aaaaa"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_multiple_characters(self):
        data = "hello world"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_empty_string(self):
        data = ""
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_repeated_characters(self):
        data = "aaaaabbbbbcccccddddd"*5
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_unique_characters(self):
        data = "abcdefghijklmnopqrstuvwxyz"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_special_characters(self):
        data = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_mixed_case_characters(self):
        data = "Hello World! 123 ABC abc"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_long_string(self):
        data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nulla sit amet aliquam lacinia, nisl nisl aliquam nisl, nec aliquam nisl nisl sit amet nisl. Sed euismod, nulla sit amet aliquam lacinia, nisl nisl aliquam nisl, nec aliquam nisl nisl sit amet nisl."*100
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_unicode_characters(self):
        data = "Hello, 世界! こんにちは! 안녕하세요!"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_newline_characters(self):
        data = "Hello\nWorld\n123\nABC\nabc"
        encoded, tree = huffman_encoding(data)
        decoded = huffman_decoding(encoded, tree)
        self.assertEqual(data, decoded)

    def test_encoded_size(self):
        data = "The bird is the word"
        
        encoded_data, tree = huffman_encoding(data)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertLess(sys.getsizeof(int(encoded_data, base=2)), sys.getsizeof(data))
        self.assertEqual(data, decoded_data)

    def test_encoded_size_repeated_characters(self):
        data = "AAAAAAABBBCCCCCCCDDEEEEEE"
 
        encoded_data, tree = huffman_encoding(data)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertLess(sys.getsizeof(int(encoded_data, base=2)), sys.getsizeof(data))
        self.assertEqual(data, decoded_data)

if __name__ == '__main__':
    unittest.main()
