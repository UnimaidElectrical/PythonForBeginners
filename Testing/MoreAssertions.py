import unittest

#Testing the identicality of objects
class TestIdentities(unittest.TestCase):
    def test_identicality(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

       #Use assert equal 
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        
        #use Is or IsNot()
        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)


#Testing truthiness and falsiness
class TruthinessAndFalsinessTests(unittest.TestCase):
    
    #Test truthiness
    def test_truthiness(self):
        self.assertTrue(3 < 5)
        self.assertTrue(1)
        self.assertTrue("hello" == "hello")
        self.assertTrue(22 > 3)

    #assert falsiness
    def test_falsiness(self):
        self.assertFalse(1 > 5)
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse({})



#AssertIn or AssertNotIn
class InorNotTests(unittest.TestCase):
    
    #AssertIn - inclusion
    def test_inclusion(self):
        self.assertIn(66, range(10, 100))
        self.assertIn("a", "Haruna")
        self.assertIn("boy", {"boy": 12, "girl": 14}.keys())
        
    #AssertNotIn - Inclusion
    def test_non_inclusion(self):
        self.assertNotIn("Tega", {"Alhamdu": 39, "Haroun": 33}.values())
        self.assertNotIn("b", "Haruna")
        self.assertNotIn(4, (5, 9, 33))
      


#Check if an object is an instance of a given class
class TestObjects(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(4, int)
        self.assertIsInstance({"a": 1, "b": 2}, dict)
        self.assertIsInstance([2,3,4], list)
        self.assertIsInstance(True, bool)
        self.assertIsInstance({1, 2, 3}, set)
        self.assertIsInstance((1, 2, 3), tuple)
        self.assertIsInstance(0.8, float)
    
    #Not an instance of
    def test_not_instance(self):
        self.assertNotIsInstance(4, dict)
        self.assertNotIsInstance({1, 2, 3}, tuple)
        self.assertNotIsInstance((1, 2, 3), set)
        self.assertNotIsInstance(8, float)
        self.assertNotIsInstance({4,5,3}, list)

#Raising errors
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_divide_option(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
