
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MyMagicCards
#   - An application to track and categorize Magic: The Gathering cards
#   - Created by Andrew Miller, FEB 06 2022
#

import csv

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classes
#   - Card
#   - Deck
#   - Player
#

class Card:

    STR_FORMAT = '''Card #%02d:
    name\t= \"%s\"
    mana_cost\t= %d
    spell_type\t= %s
    set\t\t= %s
    text\t= \"%s\"
    power\t= %d
    toughness\t= %d'''

    next_id = 0

    @staticmethod
    def __get_next_id__() -> int:
        Card.next_id += 1
        return Card.next_id

    @staticmethod
    def to_string(card):
        if card is not None:
            return Card.STR_FORMAT % (card.id, card.name, card.mana_cost, card.spell_type, card.set, card.text, card.power, card.toughness)

    def __init__(self, name:str, mana_cost, spell_type, set, text, power:int, toughness:int):
        self.id = self.__get_next_id__()
        self.name = name
        self.mana_cost = mana_cost
        self.spell_type = spell_type
        self.set = set
        self.text = text
        self.power = power
        self.toughness = toughness

    def is_match(self, check_card) -> bool:
        return self.id is check_card.id or self.name is check_card.name

class Deck:

    next_id = 0
    
    @staticmethod
    def __get_next_id__() -> int:
        Deck.next_id += 1
        return Deck.next_id

    def __init__(self, name:str, card_set:list=list()):
        self.id = self.__get_next_id__()
        self.name = name
        self.card_set = card_set
    
    def contains(self, check_card:Card) -> bool:
        for deck_card in self.card_set:
            if check_card.is_match(deck_card):
                return True
            else:
                return False

    def insert(self, card:Card) -> bool:
        if self.contains(card):
            return False
        else:
            self.card_set.append(card)
            return True

class Player:

    next_id = 0

    def __init__(self, name:str, card_set:list=list(), deck_set:list=list()):
        self.id = self.__get_next_id__()
        self.name = name
        self.card_set = card_set
        self.deck_set = deck_set
    
    @staticmethod
    def __get_next_id__() -> int:
        Player.next_id += 1
        return Player.next_id

    def add_card(self, card) -> None:
        self.card_set.append(card)
        return

    def add_deck(self, deck) -> None:
        self.deck_set.append(deck)
        for card in deck.card_set:
            self.add_card(card)
        return

#
# End Classes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Script
#

# Constants
NAME = "Andrew"
CARDFILE = "./mytestcards.csv"

# Functions
def load_cardfile(filename:str) -> list:
    card_set = list()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            card_set.append(Card(row[0], int(row[1]), row[2], row[3], row[4], int(row[5]), int(row[6])))
    return card_set

# Variables
my_player = Player(NAME)
my_deck = Deck("Deck A")
file_cards = load_cardfile(CARDFILE)
for card in file_cards:
    my_deck.insert(card)

# add deck to player
my_player.add_deck(my_deck)

# print player cards
for card in my_player.card_set:
    print(Card.to_string(card))

#
# End Script
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
