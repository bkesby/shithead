#!/usr/bin/env python
"""
Deck testing functions.
"""

import unittest

from shithead.core import Deck


class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deck = Deck()

    # Ensure correct deck length
    def test_length(self):
        self.assertEqual(len(self.deck.cards), 52)

    # Ensure all cards are unique
    def test_unique(self):
        pass


if __name__ == "__main__":
    unittest.main()
