from unittest import TestCase


class TestCard(TestCase):
    def test_get_suit(self):
        c = Card('spade', 'jack')
        self.assertEqualTest(c, 'spades')
