import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
    
    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)
    
    def test_swapcase(self):
        self.assertEqual("haruna".swapcase(), "HARUNA")
    
    def test_index(self):
        self.assertEqual("Haruna".index("H"), 0)

if __name__ == "__main__":
    unittest.main()