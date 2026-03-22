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

        def move_player(self, player, roll):
            """
            This function moves the player around the board based on the dice roll. The board wraps around when the end is reached and if player passes go,
            they receive $1
            Args:
            player (Player): player taking the turn
            roll(int): Dice roll value
            """
            board_size = len(self.board)

            old_pos = player.position

            #wraps around movement using modulo
            new_pos = (old_pos + roll) % board_size

            # if player crosses the board boundary, the player passes GO suare
            if old_pos + roll >= board_size:
                player.money +=1

            player.position = new_pos