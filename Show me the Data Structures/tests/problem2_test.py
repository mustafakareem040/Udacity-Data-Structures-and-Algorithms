import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problem2 import *
import os
import unittest

class TestFindFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for testing
        self.temp_dir = "temp_dir"
        os.makedirs(self.temp_dir)
        os.makedirs(os.path.join(self.temp_dir, "subdir1"))
        os.makedirs(os.path.join(self.temp_dir, "subdir2"))
        with open(os.path.join(self.temp_dir, "file1.txt"), "w") as f:
            f.write("ss")
        with open(os.path.join(self.temp_dir, "subdir1", "file2.txt"), "w") as f:
            f.write("")
        with open(os.path.join(self.temp_dir, "subdir2", "file3.txt"), "w") as f:
            f.write("#")
        with open(os.path.join(self.temp_dir, "subdir2", "file4.jpg"), "w") as f:
            f.write("File")
        with open(os.path.join(self.temp_dir, "subdir2", "file5.cpp"), "w") as f:
            f.write("")
    def tearDown(self):
        # Clean up the temporary directory structure
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.temp_dir)

    def test_files(self):
        suffix = ".txt"
        expected_paths = [
            os.path.join(self.temp_dir, "file1.txt"),
            os.path.join(self.temp_dir, "subdir1", "file2.txt"),
            os.path.join(self.temp_dir, "subdir2", "file3.txt")
        ]
        self.assertCountEqual(find_files(suffix, self.temp_dir), expected_paths)

    def test_find_files_with_nonexistent_suffix(self):
        suffix = ".py"
        expected_paths = []
        self.assertCountEqual(find_files(suffix, self.temp_dir), expected_paths)

    def test_find_files_with_empty_suffix(self):
        suffix = ""
        expected_paths = [
            os.path.join(self.temp_dir, "file1.txt"),
            os.path.join(self.temp_dir, "subdir1", "file2.txt"),
            os.path.join(self.temp_dir, "subdir2", "file3.txt"),
            os.path.join(self.temp_dir, "subdir2", "file4.jpg"),
            os.path.join(self.temp_dir, "subdir2", "file5.cpp")
        ]
        self.assertCountEqual(find_files(suffix, self.temp_dir), expected_paths)

    def test_find_files_with_nonexistent_directory(self):
        suffix = ".txt"
        nonexistent_dir = os.path.join(self.temp_dir, "nonexistent_dir")
        with self.assertRaises(FileNotFoundError):
            find_files(suffix, nonexistent_dir)

    def test_find_files_with_file_path(self):
        suffix = ".txt"
        file_path = os.path.join(self.temp_dir, "file1.txt")
        expected_paths = [file_path]
        self.assertCountEqual(find_files(suffix, file_path), expected_paths)

    def test_find_files_with_file_path_and_unmatched_suffix(self):
        suffix = ".c"
        file_path = os.path.join(self.temp_dir, "file1.txt")
        expected_paths = []
        self.assertCountEqual(find_files(suffix, file_path), expected_paths)

if __name__ == "__main__":
    unittest.main()
