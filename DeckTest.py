import unittest
from deck import Deck
from card import Card

class DeckTest(unittest.TestCase):
    def test_str(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_stack(self):
        deck = Deck()
        deck.stack('deck.txt')
        c = deck.draw()
        c.flip()
        AH = Card('ace', 'hearts')
        AH.flip()
        self.assertEqual(c, AH)



if __name__ == '__main__':
    unittest.main()
