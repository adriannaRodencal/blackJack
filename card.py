
class Card(object):

    def __init__(self, suit, name):
        self.__suit = suit
        self.__name = name
        self.__cardUni = self.card_uni(suit)
        self.__color = self.card_color(suit)
        self.__hardValue = self.card_value(name, 'c')
        self.__softValue = self.card_value(name, 'g')
        self._visible = False



    def __str__(self):
        if self._visible == True:
            string = ''
            string += f'Card: {self.__color}, '
            string += f'{self.__suit} of {self.__name} {self.__cardUni}'
            string += f'\nCard Value: {self.__hardValue} '
            string += f'\nGame Value: {self.__softValue}'
            return string
        else:
            string = ''
            string += 'This card is face down. All information is hidden.'
            return string

    def get__suit(self):
        return self.__suit

    def get__name(self):
        return self.__name

    def get_cardUni(self):
        return self.__cardUni

    def get_color(self):
        return self.__color

    def get_hardValue(self):
        return self.__hardValue

    def get_softValue(self):
        return self.__softValue

    def get_visible(self):
        if self._visible == False:
            return ('This card is face down, you may not see this information')
        else:
            return True

    def set_visible(self, boolean):
        self._visible = boolean

    def card_uni(self, suit):
        if suit == 'heart':
            return f'\u2665'
        elif suit == 'diamond':
            return f'\u2666'
        elif suit == 'spade':
            return f'\u2660'
        elif suit == 'club':
            return f'\u2663'

    def card_color(self, suit):
        if suit in ('diamond', 'heart'):
            return'red'
        elif suit in ('spade', 'club'):
            return 'black'

    def card_value(self, name, p):
        if name == 'ace':
            if p == 'g':
                return 1, 11
            else:
                return '1'
        elif name == 'two':
            return '2'
        elif name == 'three':
            return '3'
        elif name == 'four':
            return '4'
        elif name == 'five':
            return '5'
        elif name == 'six':
            return '6'
        elif name == 'seven':
            return '7'
        elif name == 'eight':
            return '8'
        elif name == 'nine':
            return '9'
        elif name == 'ten':
            return '10'
        elif name == 'jack':
            return '10'
        elif name == 'queen':
            return '10'
        elif name == 'king':
            return '10'

    def flip(self):
        if self._visible == True:
            self.set_visible(False)
        else:
            self.set_visible(True)


