import unittest
from cardCollection import CardCollection

class CardCollectionTesting(unittest.TestCase):
    def test_collection(self):
        selfList = ['A of H', 'A of D', 'A of C']
        self.assertEqual(selfList, ['A of H', 'A of D', 'A of C'])
        self.assertNotEqual(selfList, ['A of C', 'A of D', 'A of H'])

    def test_shuffle(self):
        selfList = ['A of H, A of D, A of C']
        CardCollection.shuffle(selfList)
        self.assertNotEqual(selfList, ['A of H', 'A of D', 'A of C'])

    def test_draw(self):
        selfList = ['A of H', 'A of D', 'A of C']
        CardCollection.draw(selfList)
        self.assertEqual(selfList, ['A of D', 'A of C'])
        self.assertNotEqual(selfList, ['A of H', 'A of D', 'A of C'])
        self.assertEqual(len(selfList), 2)

if __name__ == '__main__':
    unittest.main()
