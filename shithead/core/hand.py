#!/usr/bin/env python
"""
Hand class that is controlled by the Player.
"""
from shithead.core import Card


class Hand:
    """Hand class with knowledge of card state."""

    def __init__(self):
        # Initialize hand positions
        self.positions = {
            'hand': [],
            'top': [],
            'bottom': [],
        }

    @property
    def active(self) -> list:
        """Return the currently active position."""

        # Works for dealing only
        if len(self.positions['bottom']) < 3:
            return self.positions['bottom']
        elif len(self.positions['top']) < 3:
            return self.positions['top']
        else:
            return self.positions['hand']

    def add(self, card: Card) -> None:
        """Add the given card to the correct position."""
        self.active.append(card)

    def pop(self, idx):
        """Return selected card from the hand."""
        return self.active.pop(idx)


if __name__ == "__main__":
   pass
