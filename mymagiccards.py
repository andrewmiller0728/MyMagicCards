
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MyMagicCards
#   - An application to track and categorize Magic: The Gathering cards
#   - Created by Andrew Miller, FEB 06 2022


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Classes
#   - Card
#   - Deck
#   - Player

class Card:

    next_id = 0

    def __init__(self, name:str, mana_cost, spell_type, set, text, power:int, toughness:int):
        self.id = self.__get_next_id__()
        self.name = name
        self.mana_cost = mana_cost
        self.spell_type = spell_type
        self.set = set
        self.text = text
        self.power = power
        self.toughness = toughness

    @staticmethod
    def __get_next_id__():
        Card.next_id += 1
        return Card.next_id
    
class Deck:

    next_id = 0
    
    def __init__(self, name:str, card_set:list=None):
        self.id = self.__get_next_id__()
        self.name = name
        self.card_set = card_set

    @staticmethod
    def __get_next_id__():
        Deck.next_id += 1
        return Deck.next_id

class Player:

    next_id = 0

    def __init__(self, name:str, card_set:list=None, deck_set:list=None):
        self.id = self.__get_next_id__()
        self.name = name
        self.card_set = card_set
        self.deck_set = deck_set
    
    @staticmethod
    def __get_next_id__():
        Player.next_id += 1
        return Player.next_id

# End Classes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Script

MY_NAME = "Andrew"

my_player = Player(MY_NAME)

# End Script
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
