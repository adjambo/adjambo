import io
import sys
import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        affiche()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "1...100")  # à remplacer par le résultat attendu

if __name__ == "__main__":
    unittest.main()
