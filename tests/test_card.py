#!/usr/bin/env python
"""
Tests for the Card data class.
"""
import unittest

from shithead.common.core import Card


class TestCard(unittest.TestCase):
    
    # Test Card creation and values
    def test_card(self):
        card = Card('Heart', 1)
        self.assertEqual(card.value, 1)
        self.assertEqual(card.suit, 'heart')
        # Failed creation
        with self.assertRaises(TypeError):
            error = Card(22, 1)
            error = Card('heart', 'str')

        with self.assertRaises(ValueError):
            error = Card('something', 2)
            error = Card('heart', 0)
            error = Card('heart', 15)
            del error
        
    # Test card ordering is correct
    def test_order(self):
        pass
    
    # Test if comparing cards can be done
    def test_comparisons(self):
        card1 = Card('heart', 1)
        card2 = Card('spade', 1)
        card3 = Card('heart', 4)

        self.assertTrue(card1 == card2)
        self.assertFalse(card1 == card3)
        self.assertFalse(card2 == card3)
        self.assertTrue(card1 == 1)
        self.assertFalse(card1 != 1)
        self.assertFalse(card1 == 'one')

if __name__ == "__main__":
    unittest.main()
