"""
Install pkgs needed:
    pip install coverage

Run test:
    coverage run functions/unit_test.py
    coverage report
    coverage html
"""

import unittest

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

class TestPrimeNumber(unittest.TestCase):
    def test_less_than_one(self):
        self.assertFalse(is_prime_number(0))
        self.assertFalse(is_prime_number(1))
    
    def test_is_prime_number(self):
        self.assertTrue(is_prime_number(2))
        self.assertTrue(is_prime_number(3))
        self.assertTrue(is_prime_number(5))
        
    def test_not_prime_number(self):
        self.assertFalse(is_prime_number(4))
        self.assertFalse(is_prime_number(6))
        self.assertFalse(is_prime_number(9))

if __name__ == '__main__':
    unittest.main()
