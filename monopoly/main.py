from game import Property, Game
import json


def load_board(path):
    """
    This function loads the Monopoloy board from the provided JSON file

    The file defines each space on the board. If the space is a property, it will be convered object. Otherwise (GO), it is stored as the raw dictionary
    :param path: file path to load the board json file
    :return: a list returning the board spaces in order, property spaces are property objects, others are dictionaries
    """

    with open(path) as f:
        data = json.load(f)


    board = []

    for space in data:
        # conert property spaces into Property objects
        if space["type"] == "property":
            board.append(Property(space["name"], space["price"], space["colour"]))
        else:
            #non property spaces (GO)
            board.append(space)

    return board

def load_rolls(path):
    """
    Loads the predefined dice rolls from any json file
    These rolls determine how far the player moves each turn, because of this the game is deterministic.
    :param path: File path to the dice roles from JSON file
    :return: List of dice roll values
    """

    with open(path) as f:
        return json.load(f)
    
board = load_board("board.json")
rolls1 = load_rolls("rolls_1.json")
rolls2 = load_rolls("rolls_2.json")

# print(board)
# print(rolls1)
# print(rolls2)


board = [
    {"type": "go"},
    Property("Red1", 2, "red"),
    Property("Red2", 2, "red"),
    Property("Blue1", 3, "blue"),
]

game = Game(board)
player = game.players[0]

print("=== TEST MOVE PLAYER ===")
print(f"Start position: {player.position}, money: {player.money}")

game.move_player(player, 2)

print(f"After move: position={player.position}, money={player.money}")

print("\n=== TEST BUY PROPERTY ===")

player.position = 1  # land on Red1
game.handle_space(player)

print(f"Money after buying: {player.money}")
print(f"Owner of Red1: {board[1].owner.name}")
print(f"Player properties: {[p.name for p in player.properties]}")


print("\n=== TEST RENT (NORMAL) ===")

player2 = game.players[1]

# player1 owns Red1 already
player2.position = 1
game.handle_space(player2)

print(f"Player2 money after rent: {player2.money}")
print(f"Player1 money after receiving rent: {player.money}")

print("\n=== TEST DOUBLE RENT ===")

# give player ownership of ALL red properties
board[2].owner = player
player.properties.append(board[2])

rent = game.calculate_rent(board[1])

print(f"Calculated rent (should be doubled): {rent}")

print("\n=== TEST BANKRUPTCY ===")

player2.money = 1  # force low money
player2.position = 1

game.handle_space(player2)

print(f"Player2 money: {player2.money}")
print(f"Player2 bankrupt: {player2.bankrupt}")


print("\n=== TEST RESULTS FUNCTION ===")

result = game.results()

print("Winner:", result["WINNER: "])
print("Players:")

for p in result["players: "]:
    print(f"Name: {p['name']}, Money: {p['money']}, Position: {p['position']}")


print("\n=== TEST RESULTS WITH CONTROLLED VALUES ===")

# manually set values
game.players[0].money = 10
game.players[1].money = 5
game.players[2].money = 8
game.players[3].money = 15

result = game.results()

print("Expected winner: Sweedal")
print("Actual winner:", result["WINNER: "])

for p in result["players: "]:
    print(p)

