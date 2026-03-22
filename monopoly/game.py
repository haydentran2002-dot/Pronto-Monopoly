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

        def handle_space(self,player):
            """
            Handles the action that occurs whenver a player lands on a space.

            POSSIBLE OUTCOMES:
            - If space is unowned -> player must buy it
            - If space is owned by another player -> pay rent
            - If player cannot afford rent -> bankruptcy occurs

            args: player (Player): Player who landed on the space
            """

            space = self.board[player.position]

            if isinstance(space, Property):

                # if unowned player must buy it. OR if they do not have enough to buy do nothing
                if space.owner is None:
                    if player.money >= space.price:
                        player.money -= space.price
                        space.owner = player
                        player.properties.append(space)

                # if owned by another player, rent must be paid

                elif space.owner != player:

                    rent = self.calculate_rent(space) #will create this function later, but just have it  here for now

                    #transfer rent
                    player.money -= rent
                    space.owner.money += rent

                    #check bankruptcy condition

                    if player.money < 0:
                        player.bankrupt = True

        def calculate_rent(self, property):
            """
            This function helps calculate the rent owned when landing on a property.

            Rent rules:
            - base rent equals the property's price
            - if owner owns ALL properties of that color, rent is doubled

            Args:
                property (Property): Property being landed on

            Return:
                int: rent amount
            """

            # First we want to find all properties on the board with the same colour
            same_colour = [] # append all instances with same colour as inputted property here
            for p in self.board:
                if isinstance(p, Property) and p.colour == property.colour: #makes sure that we check Properties only
                    same_colour.append(p)

            # Check if owner owns all of these
            if all(p.owner == property.owner for p in same_colour): # checks if every property ins ame_colour has the same owner as property_owner
                return property.price * 2
            
            return property.price #return normal price if owner doesn't own all
        

        def play(self, rolls):
            """
            Simulates the full game using sequence of dice rolls
            Player take turns in order and will immediately end when a player becomes bankrupt
            Or just ends when all the rolls are up and no one bankrupt

            Args:
                rolls (list[int]): Predetermined dice roll sequence
            """

            turn = 0

            while turn < len(rolls):

                # determine which players turn it is
                player = self.players[turn % len(self.players)]
                roll = rolls[turn]

                self.move_player(player, roll)
                self.handle_space(player)

                # stop immediately when someone goes bankrupt
                if player.bankrupt:
                    break

                turn += 1