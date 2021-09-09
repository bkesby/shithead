#!/usr/bin/env python
"""
Dealer class to act as game manager to handle all game components.
"""

from shithead.core import Deck


class Dealer:
    """Game manager that controls all core components."""

    def __init__(self):
        """Initialize all game components."""

        # Create the deck and prepare
        self.deck = Deck()
        self.deck.shuffle()

        # Collect Players
        self.players = []

    def deal(self):
        """Deal out cards to all players from top of deck."""

        # Loop until all players have enough cards
        # Add the next card from deck to each player Hand
        pass


if __name__ == "__main__":
    pass
