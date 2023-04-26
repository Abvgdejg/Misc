import string

class Card:

    id = None

    name = None
    description = None

    set = None
    number = None

    fraction = None
    rarity = None

    cost = None

    health = None
    stamina = None
    damage = None
    
    image = None

    def __init__(self, id, name, description, set, number, fraction, rarity, cost, health, stamina, damage, image):

        self.id = id

        self.name = name
        self.description = description

        self.set = set
        self.number = number

        self.fraction = fraction
        self.rarity = rarity

        self.cost = cost

        self.health = health
        self.stamina = stamina
        self.damage = damage
        
        self.image = image

    def __repr__(self) -> str:
        
        return str(self.name)

class CardSets:
    VarOfElements = 1

class Deck():

    name = "Deck"
    deck = []

    def __init__(self, cards, name="Deck"):
        self.name = name
        self.deck = []
        
        for card in cards:
            self.__add__(card)


    def __repr__(self) -> str:
        returned_str = "==========\n\n"
        returned_str += f"### Deck: {self.name} ###\n\n"
        for card in self.deck:
            returned_str += str(card[0]) + " X " + str(card[1]) + "\n"
        
        returned_str += "\n######\n\n"
        returned_str += str(self.create_code()) 
        returned_str += "\n\n######"
        returned_str += "\n\n=========="

        return returned_str

    def __add__(self, card: Card):
        for d_card in self.deck:
            if d_card[0] == card: 
                d_card[1] += 1
                return
        
        self.deck.append([card, 1])

    def create_code(self):
        code = ""
        code_list = []

        chars = [f"{first}{second}" for first in string.ascii_letters for second in string.digits ]

        for card in self.deck:

            card_code = chars[int(str(CardSets.VarOfElements) + card[0].number)]
            code_list.append(str(card[1]) + card_code)

        code = ':'.join(code_list)
        return code

    def deck_from_code(code, card_list):
        chars = [f"{first}{second}" for first in string.ascii_letters for second in string.digits ]

        deck = []
        cards = code.split(":")

        for card in cards:
            
            count = int(card[0:1:])
            card_data = card[1::]
            card_data = chars.index(card_data)
            card_set = str(card_data)[0:1:]
            card_number = str(card_data)[1:]
            deck_card = None
            
            for i_card in card_list:
                if i_card.number != card_number: continue
                deck_card = i_card

            for i in range(count):
                deck.append(deck_card)

        return Deck(deck)