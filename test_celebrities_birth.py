#%%

import unittest
from structure_example.celebrities_births import Date

class DateTest(unittest.TestCase):
    
    def setUp(self):
        self.new_date = Date(30, 10, 2021)
        
    def test_date_valid(self):
        self.assertEqual(True, self.new_date.is_date_valid(30, 10, 2021))
        
    def test_wiki_format(self):
        self.assertEquals('October_30', self.new_date.to_wiki_format())
    

unittest.main(argv=[''], verbosity=2, exit=False)

#%%