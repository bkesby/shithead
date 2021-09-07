#!/usr/bin/env python
"""
Deck testing functions.
"""

import unittest

from shithead.common.core import Deck


class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deck = Deck()

    # Ensure correct deck length
    def test_length(self):
        self.assertEqual(len(self.deck.cards), 52)
    
if __name__ == "__main__":
    unittest.main()