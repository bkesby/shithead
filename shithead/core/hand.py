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
            "hand": [],
            "top": [],
            "bottom": [],
        }

    @property
    def active(self) -> list:
        """Return the currently active playing position."""

        if len(self.positions["hand"]) > 0:
            return self.positions["hand"]
        elif len(self.positions["top"]) > 0:
            return self.positions["top"]
        else:
            return self.positions["bottom"]

    def add(self, card: Card, pos="hand") -> None:
        """Add the given card to the hand, or specified position."""
        self.positions[pos].append(card)

    def pop(self, idx):
        """Return selected card from the hand."""
        return self.active.pop(idx)


if __name__ == "__main__":
    pass
