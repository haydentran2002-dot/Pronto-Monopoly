class Player:
    def __init__(self, name):
        self.name = name
        self.money = 16
        self.position = 0
        self.properties = []
        self.bankrupt = False

class Property:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
        self.owner = None 

    def __repr__(self): # used to help see the output my clearly adn check that the json file import worked
        return f"Property(name={self.name}, price={self.price}, colour={self.colour}, owner={self.owner.name if self.owner else None})"
    

class Game:
    def __init__(self, board):
        self.board = board
        self.players = {
            Player("Peter"),
            Player("Billy"),
            Player("Charlotte"),
            Player("Sweedal")
        }