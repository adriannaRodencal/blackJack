from card import Card
from cardCollection import CardCollection

class Deck(CardCollection):

    def __init__(self):
        super().__init__()
        for name in Card.names:
            for suit in Card.suits:
                newCard = Card(name, suit)
                self.append(newCard)

    def stack(self, deckFile = 'deck.txt'):
        """
        Clear the current deck and restack a new deck.
        :param deckFile
        :return none
        """
        #
        # Clear the current list to restack
        #
        self.clear()
        with open(deckFile, 'r') as endFile:
            for line in endFile:
                suit, name = line.split(', ')
                card = Card(name.strip(), suit)
                self.append(card)

