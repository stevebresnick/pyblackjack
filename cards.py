import random

class Deck():
    cards = []

    def __init__(self):
        self.cards = [
        {'name':'Ace', 'suit':'Spades', 'value':11},
        {'name':'Ace', 'suit':'Clubs', 'value':11},
        {'name':'Ace', 'suit':'Hearts', 'value':11},
        {'name':'Ace', 'suit':'Diamonds', 'value':11},
        {'name':'2', 'suit':'Spades', 'value':2},
        {'name':'2', 'suit':'Clubs', 'value':2},
        {'name':'2', 'suit':'Hearts', 'value':2},
        {'name':'2', 'suit':'Diamonds', 'value':2},
        {'name':'3', 'suit':'Spades', 'value':3},
        {'name':'3', 'suit':'Clubs', 'value':3},
        {'name':'3', 'suit':'Hearts', 'value':3},
        {'name':'3', 'suit':'Diamonds', 'value':3},
        {'name':'4', 'suit':'Spades', 'value':4},
        {'name':'4', 'suit':'Clubs', 'value':4},
        {'name':'4', 'suit':'Hearts', 'value':4},
        {'name':'4', 'suit':'Diamonds', 'value':4},
        {'name':'5', 'suit':'Spades', 'value':5},
        {'name':'5', 'suit':'Clubs', 'value':5},
        {'name':'5', 'suit':'Hearts', 'value':5},
        {'name':'5', 'suit':'Diamonds', 'value':5},
        {'name':'6', 'suit':'Spades', 'value':6},
        {'name':'6', 'suit':'Clubs', 'value':6},
        {'name':'6', 'suit':'Hearts', 'value':6},
        {'name':'6', 'suit':'Diamonds', 'value':6},
        {'name':'7', 'suit':'Spades', 'value':7},
        {'name':'7', 'suit':'Clubs', 'value':7},
        {'name':'7', 'suit':'Hearts', 'value':7},
        {'name':'7', 'suit':'Diamonds', 'value':7},
        {'name':'8', 'suit':'Spades', 'value':8},
        {'name':'8', 'suit':'Clubs', 'value':8},
        {'name':'8', 'suit':'Hearts', 'value':8},
        {'name':'8', 'suit':'Diamonds', 'value':8},
        {'name':'9', 'suit':'Spades', 'value':9},
        {'name':'9', 'suit':'Clubs', 'value':9},
        {'name':'9', 'suit':'Hearts', 'value':9},
        {'name':'9', 'suit':'Diamonds', 'value':9},
        {'name':'10', 'suit':'Spades', 'value':10},
        {'name':'10', 'suit':'Clubs', 'value':10},
        {'name':'10', 'suit':'Hearts', 'value':10},
        {'name':'10', 'suit':'Diamonds', 'value':10},
        {'name':'Jack', 'suit':'Spades', 'value':10},
        {'name':'Jack', 'suit':'Clubs', 'value':10},
        {'name':'Jack', 'suit':'Hearts', 'value':10},
        {'name':'Jack', 'suit':'Diamonds', 'value':10},
        {'name':'Queen', 'suit':'Spades', 'value':10},
        {'name':'Queen', 'suit':'Clubs', 'value':10},
        {'name':'Queen', 'suit':'Hearts', 'value':10},
        {'name':'Queen', 'suit':'Diamonds', 'value':10},
        {'name':'King', 'suit':'Spades', 'value':10},
        {'name':'King', 'suit':'Clubs', 'value':10},
        {'name':'King', 'suit':'Hearts', 'value':10},
        {'name':'King', 'suit':'Diamonds', 'value':10},
        ]

    #shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #return value of cards
    def get_value(self,cards):
        value = 0
        for card in cards:
            value = card['value'] + value
        return value

    #deal a card
    def deal(self,deck,hand,dealtcards):
        shoe = deck #must be a list
        playerhand = hand #must be a list
        count = 0
        while count < dealtcards:
            card = shoe.pop()
            playerhand.append(card)
            count = count + 1
