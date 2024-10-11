import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        self.assertEqual(affiche(), "1Fizz2Buzz...")  # Remplace par le résultat attendu

if __name__ == "__main__":
    unittest.main()
