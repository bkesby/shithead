#!/usr/bin/env python
"""
Core game component file. Contains game object classes.
"""
from dataclasses import dataclass


@dataclass
class Card:
    """Class for holding card values."""
    suit: str
    value: int
    

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

class Dealer:
    """Unique card handler."""

    def __init__(self):
        """Initialize all game components."""

        self.round = 0
        self.turn = 0

        self.deck = Deck()

if __name__ == "__main__":
    pass
