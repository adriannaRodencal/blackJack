import random

class CardCollection(list):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        if len(self) == 0:
            string = 'No card in deck'
        else:
            string = '['
            for card in self:
                string += str(card) + ', '
            string = string[:-2] + ']'
        print(string)
        return string

    def shuffle(self):
        """
        Shuffle card within deck
        :param none
        :return none
        """
        for newCards in range(1, len(self)):
            writeCard = random.randint(0, newCards)
            if writeCard != newCards:
                self[newCards], self[writeCard] = self[writeCard], self[newCards]

    def draw(self):
        """
        Once card is drawn from collection delete it
        :param none
        :return none
        """
        if len(self) > 0:
            card = self.pop(0)
        else:
            raise ValueError('There are 0 cards in this deck')
        return card




