from card import Card

def card_test1():
    print('____ Card 1 ____')
    print('~~Unturned')
    t1 = Card('spade', 'jack')
    print(t1)
    print('~~Turned')
    t1.set_visible(True)
    print(t1)
    print()

def flip_test():
    print('____ Card Flip ____')
    print('~~Face Down')
    t2 = Card('heart', 'ace')
    print(t2)
    t2.flip()
    print('~~Flip')
    print(t2)
    print()

def deck_test():
    print('____ Deck Test ____')
    with open('deck.txt', 'r') as deckFile:
        for line in deckFile:
            suit, name = line.split(',')
            suit = suit.strip()
            name = name.strip()
            t3 = Card(suit, name)
            t3.set_visible(True)
            print(t3)

if __name__ == '__main__':
    card_test1()
    flip_test()
    deck_test()