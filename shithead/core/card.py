#!/usr/bin/env python
"""
Card data class to be used by Deck.
"""


class Card:
    """Class for holding card values."""

    suits = {'c': 'club', 'd': 'diamond', 'h': 'heart', 's': 'spade'}

    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, x):
        # Type check
        if type(x) != str:
            raise TypeError('Attribute suit should be of type `str`')

        # Always create lower case
        x = x.lower()

        # Assign full value if abbreviation is used
        if x in self.suits.keys():
            self.__suit = self.suits[x]
        elif x in self.suits.values():
            self.__suit = x
        else:
            raise ValueError(f'Attribute suit must be one of {self.suits.values()}')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):
        # Type check
        if type(x) != int:
            raise TypeError('Attribute value should be of type `int`')

        # Ensure set value is in valid range
        if not x in range(2,15):
            raise ValueError('Attribute value must be in the range of 2 >= 14')
        else:
            self.__value = x

    # ====================================================================== #
    #                               Comparisons                              #
    # ====================================================================== #
    def __eq__(self, o: object) -> bool:
        # Only use value of class to compare
        if isinstance(o, Card):
            return self.value == o.value
        elif isinstance(o, int):
            return self.value == o
        else:
            return False

    def __ne__(self, o: object) -> bool:
        NotImplemented

    def __lt__(self, o: object) -> bool:
        if isinstance(o, Card):
            return self.value < o.value
        elif isinstance(o, int):
            return self.value < o
        else:
            return False

    def __gt__(self, o: object) -> bool:
        if isinstance(o, Card):
            return self.value > o.value
        elif isinstance(o, int):
            return self.value > o
        else:
            return False

    def __le__(self, o: object) -> bool:
        if isinstance(o, Card):
            return self.value <= o.value
        elif isinstance(o, int):
            return self.value <= o
        else:
            return False

    def __ge__(self, o: object) -> bool:
        if isinstance(o, Card):
            return self.value >= o.value
        elif isinstance(o, int):
            return self.value >= o
        else:
            return False



# TODO: Create the Deck as a Card generator. Initializing creates all cards and
# completes a shuffle()
class Deck:
    """Card Manager/Holder."""

    def __init__(self):
        """Initialize the deck of cards."""

        # Create 52 cards with no matching.
        self.cards = self.create_cards()

    def create_cards(self):
        """Create a complete deck of Cards."""

        # Initialize the return list and iterate over card creation
        cards = []
        for suit in ['Club', 'Diamond', 'Heart', 'Spade']:
            for val in range(2, 15):
                cards.append(Card(suit=suit, value=val))

        return cards

    def shuffle(self):
        """Randomise the order of Cards in the deck."""
        pass

class Dealer:
    """Unique card handler."""

    def __init__(self):
        """Initialize all game components."""

        self.round = 0
        self.turn = 0

        self.deck = Deck()

if __name__ == "__main__":
    pass
