#!/usr/bin/env python
"""
Tests for the Card data class.
"""
import unittest

from shithead.core import Card


class TestCard(unittest.TestCase):

    # Test Card creation and values
    def test_card(self):
        card = Card('H', 2)
        self.assertEqual(card.value, 2)
        self.assertEqual(card.suit, 'heart')
        # Failed creation
        with self.assertRaises(TypeError):
            error = Card(22, 2)
            error = Card('heart', 'str')

        with self.assertRaises(ValueError):
            error = Card('something', 2)
            error = Card('heart', 1)
            error = Card('heart', 18)
            del error

    # Test card ordering is correct
    def test_order(self):
        pass

    # Test if comparing cards can be done
    def test_comparisons(self):
        card1 = Card('heart', 2)
        card2 = Card('spade', 2)
        card3 = Card('heart', 4)

        # Equals
        self.assertTrue(card1 == card2)
        self.assertFalse(card1 == card3)
        self.assertFalse(card2 == card3)
        self.assertTrue(card1 == 2)
        self.assertFalse(card1 != 2)
        self.assertFalse(card1 == 'ace')

        # Greater/Less
        self.assertTrue(card1 < card3)
        self.assertFalse(card3 < card1)
        self.assertTrue(card3 > card1)
        self.assertFalse(card3 < card1)
        self.assertTrue(card1 <= card2)
        self.assertTrue(card1 <= card3)
        self.assertFalse(card1 >= card3)
        self.assertTrue(card3 >= card1)

if __name__ == "__main__":
    unittest.main()
