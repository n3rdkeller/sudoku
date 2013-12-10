__author__ = "n3rdkeller.de"
__license__ = "GPL"
__version__ = "0.9"
__email__ = "github@n3rdkeller.de"
__status__ = "Development"

# imports
import re
import os
import sys
from sudoku import ERROR
from sudoku import COLORS

# -----
# functions
# -----
def mainmenu():
    print("Welcome to our Sudoku!")
    print("This program is controlled by our command language.")
    print("For further information read the README.txt or")
    print("type 'help' or 'help {command}'.\n")

def clear_screen():
    '''Clears the terminal window.'''
    # We do really not like Windows for this to be duty.
    if os.name == "posix":
        os.system('clear')
    elif sys.stdin.encoding.lower() == "cp1252": # IDLE
        print(1000 * "\n")
    elif os.name in ("nt", "dos", "ce"):
        os.system('cls')
    else:
        print(80 * "\n")

def input_command() -> tuple:
    '''Asks the user for an input.
    Interprets it with our command language after.'''
    print("What do you want to do?")
    raw_input_str = input(COLORS["red"] + ">> " + COLORS["clear"])
    input_str = raw_input_str.upper()
    # pattern for our whole command language
    pattern = re.compile("^(ADD)\s([A-I])([1-9])\s[1-9]$|" + \
                            "^(DEL)\s([A-I])([1-9])$|^(CHK)$|" + \
                            "^(SAVE)$|^(SAVE)\s(\w{1,250})$|" + \
                            "^(LOAD)$|^(LOAD)\s(\w{1,250})$|" + \
                            "^(HELP)$|^(HELP)\s(ADD|DEL|SAVE|LOAD|CHK|QUIT|NEW)$|" + \
                            "^(QUIT)|^(NEW)")
    if pattern.match(input_str):
        if input_str[:3] == "ADD":
            return (0, input_str[4:])  # type 0 for add
        elif input_str[:3] == "DEL":
            return (1, input_str[4:])  # type 1 for del
        elif input_str[:4] == "SAVE":
            if len(input_str) == 4:
                # type 2 and empty string for default save
                return (2, "")
            else:
                return (2, raw_input_str[5:])  # type 2 and filename for save
        elif input_str[:4] == "LOAD":
            if len(input_str) == 4:
                # type 3 and empty string for default load
                return (3, "")
            else:
                return (3, raw_input_str[5:])  # type 3 and filename for load
        elif input_str[:3] == "CHK":
            return (4, "")
        elif input_str[:4] == "HELP":
            return (5, input_str[5:])
        elif input_str[:4] == "QUIT":
            return (6, "")
        elif input_str[:4] == "NEW":
            return (7, "")
    else:
        return (ERROR, "")            # type ERROR and empty string for error

def parse_help(arg: str):
    if arg == "ADD":
        print("ADD (A-I)(1-9) (1-9)")
        print("Adds a number to position specified by alphanumeric coordinates.")
        print("examples: 'ADD B3 6', 'ADD E5 3'")
    elif arg == "DEL":
        print("DEL (A-I)(1-9)")
        print("Deletes position specified by alphanumeric coordinates.")
        print("examples: 'DEL B3','DEL E5'")
    elif arg == "SAVE":
        print("SAVE {filename}")
        print("Saves the current sudoku to the given filename.")
        print("If empty, the sudoku is saved into the default file.")
        print("example: 'SAVE my_sudoku'")
    elif arg == "LOAD":
        print("LOAD {filename}")
        print("Loads a saved sudoku.")
        print("If empty, the default file is loaded.")
        print("example: 'LOAD my_sudoku'")
    elif arg == "CHK":
        print("CHK")
        print("Checks the whole sudoku for errors.")
    elif arg == "QUIT":
        print("QUIT")
        print("Quits the game without saving.")
    elif arg == "NEW":
        print("NEW")
        print("Creates empty sudoku without saving the current one.")
    else:
        print(COLORS["green"] + "HELP" + COLORS["clear"] + "  displays this help")
        print(COLORS["green"] + "ADD"  + COLORS["clear"] + "   adds a number")
        print(COLORS["green"] + "DEL"  + COLORS["clear"] + "   deletes a number")
        print(COLORS["green"] + "SAVE" + COLORS["clear"] + "  saves the sudoku")
        print(COLORS["green"] + "LOAD" + COLORS["clear"] + "  loads a sudoku")
        print(COLORS["green"] + "CHK"  + COLORS["clear"] + "   checks the whole sudoku")
        print(COLORS["green"] + "QUIT" + COLORS["clear"] + "  quits the game")
        print(COLORS["green"] + "NEW"  + COLORS["clear"] + "   creates empty sudoku")
    print()

def parse_add(arg: str) -> tuple:
    '''Parses the argument of the ADD-command
    for later using in our class "sudoku".
    Returns a 3-tuple with (x, y, number).'''
    x = arg[0]
    y = int(arg[1])
    num = int(arg[3])
    return (x, y, num)

def parse_del(arg: str) -> tuple:
    '''Parses the argument of the DEL-command
    for later using in our class "sudoku".
    Returns a pair with (x, y).'''
    x = arg[0]
    y = int(arg[1])
    return (x, y)
