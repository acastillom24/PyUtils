"""
Install pkgs needed:
    pip install freezegun
"""

import unittest
from freezegun import freeze_time

from datetime import datetime

def end_pandemic():
    
    today = datetime.today()
    if today.year > 2022:
        return True
    
    return False

class TestEndPandemic(unittest.TestCase):
    def test_end_pandemic_true(self):
        self.assertTrue(end_pandemic())
    
    @freeze_time("2021-01-01")
    def test_end_pandemic_false(self):
        self.assertFalse(end_pandemic())
    
if __name__ == '__main__':
    unittest.main()