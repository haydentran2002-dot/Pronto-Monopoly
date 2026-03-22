from game import Property
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

print(board)
print(rolls1)
print(rolls2)