import unittest

#A sample function to use for testing
def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

#Test class inherits from TestCase
class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("Heelo", "hello")
    
    #check by using assertion
    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertNotEqual(
            values, [1, 2, 3, 4],
            "Make sure your'e creating a copy"
        )

if __name__ == "__main__":
    unittest.main()