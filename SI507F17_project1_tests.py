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

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_of_cards(self):
        self.assertEqual(len(self.deck.cards), 52, 'checks to make sure that the number of cards in the deck is 52')

    def test_deck_instances(self):
        for card_object in self.deck.cards:
            self.assertIsInstance(card_object, Card, 'check to make sure that the cards created in the Deck class are isntances of the Card class')

    def test_deck_string(self):
        self.d_string = str(self.deck)
        self.d_list = self.d_string.split('\n')
        self.assertEqual(len(self.d_list), 52, "checks to make sure the Deck class's string prints out 52 lines")

    def tearDown(self):
        self.deck

class TestpopCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        for x in range(52):
            self.deck.pop_card()
        self.card = self.deck.cards

    def test_pop_card(self):
        self.assertEqual(self.card, [], 'checks to see if invoking the pop_card function 52 times leaves the deck of cards list empty')

    def tearDown(self):
        self.deck

class TestDeckSuffle(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.cards = self.deck.cards
        self.deck.shuffle()
        self.s_card = self.deck.cards

    def test_shuffle(self):
        self.assertNotEqual(self.cards, self.s_card, 'checks to see if the shuffle function returns a shuffled list of the cards (i.e. not equal lists)')

    def tearDown(self):
        self.deck
        self.cards
        self.s_card

class TestDeckReplace(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.card_strs = []
        for c in self.deck.cards:
            self.card_strs.append(c.__str__())
        if self.deck.cards.__str__() not in self.card_strs:
            self.deck.cards.append(self.deck.cards)

    def test_replace(self):
        self.assertIn('2 of Diamonds', self.card_strs, "checks to make sure the replace card doesn't duplicate")

    def tearDown(self):
        self.deck
        self.card_strs

class TestDeckPartTwo(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.deal_hand(26)

    def test_deal_hand(self):
        self.assertEqual(len(self.deck.cards), len(range(26)), "checks to make sure that when dealing 26 cards, that there are 26 cards remaining in the deck")

    def tearDown(self):
        self.deck

# class TestPlayWar(unittest.TestCase):

# class TestSong(unittest.TestCase):

if __name__ == '__main__':
    unittest.main(verbosity=2)
###########
