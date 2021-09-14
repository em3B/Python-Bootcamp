class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

from random import shuffle

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in suits:
            # Add all values to each suit in order to create a full deck 
            for value in values:
                self.cards.append(Card(value, suit)) 
        print(self.cards)

        # statement with number of cards 
    def __repr__(self):
        return "Deck of {} cards".format(self.count())

        # number of cards
    def count(self):
        return len(self.cards)

        # deal a Card and remove count from total
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        print("Going to remove {} cards".format(actual))
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

        # deal a single card
    def deal_card(self):
        return self._deal(1)[0]

        # deal a given number of cards 
    def deal_hand(self, hand_size):
        return self._deal(hand_size)

        # shurffle a full deck 
    def shuffle(self):
        if self.count()<52:
            raise ValueError("Only full decks can be shuffled") 
        shuffle(self.cards)

my_deck = Deck()
type(my_deck)
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
