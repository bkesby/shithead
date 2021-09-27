#!/usr/bin/env python
"""
Dealer class to act as game manager to handle all game components.
"""
from itertools import cycle

from shithead.core import Deck


class Dealer:
    """Game controller that manages all game components."""

    def __init__(self, players: list):
        """Initialize all game components."""

        # Create the deck and prepare
        self.deck = Deck()
        self.deck.shuffle()

        # Collect Players
        self.players = players

    def deal(self):
        """Deal out cards to all players from top of deck."""

        hand_has_room = self.players[-1].positions['hand'] < 4
        loop = cycle(self.players)

        while hand_has_room:
            player = next(loop)
            player.add(next(self.deck))
            print('card added.')

        print('all cards added!')




if __name__ == "__main__":
    pass
