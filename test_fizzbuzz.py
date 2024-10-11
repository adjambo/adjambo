import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        self.assertEqual(affiche(), "1Fizz2Buzz...")  # Mettez ici le résultat attendu
