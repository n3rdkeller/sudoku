__author__ = "n3rdkeller.de"
__license__ = "GPL"
__version__ = "0.9"
__email__ = "github@n3rdkeller.de"
__status__ = "Development"

# imports
import ui
from sudoku import Sudoku  # importing class
from sudoku import EMPTY_SUDOKU
from sudoku import ERROR
from sudoku import COLORS

# -----
# functions
# -----
def main():
    ui.mainmenu()
    s = Sudoku()
    print(s.get_str())
    while True:
        command = ui.input_command()
        if command[0] == 0:
            # ADD
            args = ui.parse_add(command[1])
            if s.check_number(args[0], args[1], args[2]) == []:
                s.add_number(args[0], args[1], args[2])
            else:
                print("The number you tried to add does not fit the rules.")
                print("Please try again.")
                continue
        elif command[0] == 1:
            # DEL
            args = ui.parse_del(command[1])
            s.del_number(args[0], args[1])
        elif command[0] == 2:
            # SAVE
            if not s.save(command[1]):
                continue
        elif command[0] == 3:
            # LOAD
            if not s.load(command[1]):
                continue
        elif command[0] == 4:
            # CHK
            if s.check():
                print(COLORS["green"] + "Your Sudoku seems right.\n" + \
                      COLORS["clear"])
            else:
                print(COLORS["red"] + COLORS["bell"] + \
                      "Your Sudoku is wrong.\n" + COLORS["clear"])
            continue
        elif command[0] == 5:
            # HELP
            ui.parse_help(command[1])
            continue
        elif command[0] == 6:
            # QUIT
            print("Quitting game...")
            exit()
        elif command[0] == 7:
            # NEW
            s.set_numbers(EMPTY_SUDOKU)
        elif command[0] == ERROR:
            # ERROR
            print("Unknown command. Please try again.")
            continue
        ui.clear_screen()
        print(s.get_str())


if __name__ == '__main__':
    main()
