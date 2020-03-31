import unittest
from card import Card

class BJ_Testing(unittest.TestCase):

    def assertEqualTest(self, c, string):
        print(string)
        self.assertEqual(c.string(), string)

class BJ_TestMethod(BJ_Testing):

    def test_get_suit(self):
        c = Card('spade', 'jack')
        self.assertEqual(c, 'spade')