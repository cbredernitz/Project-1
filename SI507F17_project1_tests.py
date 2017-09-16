## Do not change import statements.

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

import unittest
from SI507F17_project1_cards import *

class TestCards(unittest.TestCase):
    def setUp(self):
        self.card = Card()

    # def test_class_variable(self):
    #     self.assertIsInstance(type(suit_names), Card, 'checks to see if suit_names is in the Card class')
    #     self.assertIsInstance(self.card.rank_levels, Card, 'checks to see if rank_levels is in the Card class')
    #     self.assertIsInstance(self.card.faces, Card, 'checks to see if faces is in the Card class')

    def test_suit_names(self):
        self.assertEqual(self.card.suit_names,["Diamonds","Clubs","Hearts","Spades"], 'should be a list containing suits')

    def test_rank(self):
        self.assertEqual(self.card.rank_levels,[1,2,3,4,5,6,7,8,9,10,11,12,13], 'should be a list of card ranks from 0-13')

    def test_faces(self):
        self.assertEqual(self.card.faces, {1:"Ace",11:"Jack",12:"Queen",13:"King"}, 'should be a dictionary of the face card values')

# This test below could be the one that needs to fail.  retuns 'diamonds' instead of 0, but I could jsut not be itereating it through correctly
    def test_default_card_suit(self):
        self.assertEqual(self.card.suit, self.card.suit_names[0], 'default suit should be 0 or "Diamonds"')

    def test_default_card_rank(self):
        self.assertEqual(self.card.rank, 2, 'default rank should be 2')

    def test_card_string(self):
        self.card = Card(0,13)
        self.string = str(self.card)
        self.assertEqual(self.string, "King of Diamonds", 'check to see if the __str__ variable prints correctly')

    def test_card_suit_instance(self):
        self.assertIn(self.card.suit, self.card.suit_names, 'check to make sure that the suit of the card is in the suit_names variable')

    def test_card_rank_instance(self):
        self.rank = self.card.rank
        if self.rank in self.card.faces:
            self.rank = self.faces[rank]
        else:
            self.rank = self.rank
        self.assertEqual(self.card.rank, self.rank, 'check to make sure that the rank printed is either the rank level or the face')

    def test_card_rank_num_instance(self):
        self.assertIn(self.card.rank_num, self.card.rank_levels, 'check to make sure that the rank_num is in the rank_levels list')

    def tearDown(self):
        self.card


# class TestDeckPartTwo(unittest.TestCase):
#     def setUp(self):
#         self.deck = Deck()
# class TestPlayWar(unittest.TestCase):
#
# class TestSong(unittest.TestCase):

if __name__ == '__main__':
    unittest.main(verbosity=2)
###########
