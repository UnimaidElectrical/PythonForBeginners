import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])
        
    #let's test the count function
    def test_count(self):
        self.assertEqual("Haruna".count("a"), 2)

if __name__ == "__main__":
    unittest.main()
