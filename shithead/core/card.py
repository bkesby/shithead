#!/usr/bin/env python
"""
Base Card data class and the deck to use the Cards.
"""
from random import randint, shuffle


class Card:
    """Class for holding card values."""

    suits = {"c": "club", "d": "diamond", "h": "heart", "s": "spade"}
    key = {"11": "Jack", "12": "Queen", "13": "King", "14": "Ace"}

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
            raise TypeError("Attribute suit should be of type `str`")

        # Always create lower case
        x = x.lower()

        # Assign full value if abbreviation is used
        if x in self.suits.keys():
            self.__suit = self.suits[x]
        elif x in self.suits.values():
            self.__suit = x
        else:
            raise ValueError(f"Attribute suit must be one of {self.suits.values()}")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x) -> None:
        # Type check
        if type(x) != int:
            raise TypeError("Attribute value should be of type `int`")

        # Ensure set value is in valid range
        if not x in range(2, 15):
            raise ValueError("Attribute value must be in the range of 2 >= 14")
        else:
            self.__value = x

    def str_value(self) -> str:
        """Return the string repesentation of card value."""
        if self.value < 11:
            return str(self.value)
        else:
            # Using key dictionary to lookup string value
            return self.key[str(self.value)]

    def __str__(self) -> str:
        return f"{self.str_value()} of {self.suit.capitalize()}s"

    def __repr__(self) -> str:
        return f"Card({self.suit}, {self.value})"

    # ====================================================================== #
    #                             Comparisons                                #
    # ====================================================================== #
    def __hash__(self) -> int:
        return hash((self.suit, self.value))

    def __eq__(self, o: object) -> bool:
        # Only use value of class to compare
        if isinstance(o, Card):
            return self.value == o.value
        elif isinstance(o, int):
            return self.value == o
        else:
            return False

    def __ne__(self, o: object) -> bool:
        if isinstance(o, Card):
            return self.value != o.value
        elif isinstance(o, int):
            return self.value != o
        else:
            return False

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

        # Create 52 cards with no matching and assign to __cards
        self.create_cards()

    @property
    def cards(self) -> list:
        return self.__cards

    def create_cards(self) -> None:
        """Create a complete deck of Cards."""

        # Iterate over suits and cards numbers
        cards = []
        for suit in ["c", "d", "h", "s"]:
            for val in range(2, 15):
                cards.append(Card(suit, val))

        # Initialize cards set in __hidden__ attribute
        self.__cards = cards

    def shuffle(self):
        """Randomise the order of Cards in the deck."""
        shuffle(self.cards)

    def fisher_yates_shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            j = randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        return self

    def __next__(self):
        """Pop of last card and return."""
        return self.cards.pop()

    def __iter__(self):
        """Creates the class as an iterator."""
        return self

    def __str__(self) -> str:
        return f"Deck of 52 cards."

    def __repr__(self) -> str:
        return f"Deck()"


if __name__ == "__main__":
    pass
