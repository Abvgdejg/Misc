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


class Deck():

    name = "Deck"
    deck = []

    def __init__(self, cards, name="Deck"):
        self.name = name
        
        for card in cards:
            self.__add__(card)

    def __repr__(self) -> str:
        returned_str = "==========\n"
        returned_str += f"Deck: {self.name}\n"
        for card in self.deck:
            returned_str += str(card[0]) + " X " + str(card[1]) + "\n"
        returned_str += "=========="

        return returned_str

    def __add__(self, card: Card):
        for d_card in self.deck:
            if d_card[0] == card: 
                d_card[1] += 1
                return
        
        self.deck.append([card, 1])

