__author__ = "n3rdkeller.de"
__license__ = "GPL"
__version__ = "0.9"
__email__ = "github@n3rdkeller.de"
__status__ = "Development"

# imports
import pickle
import sys
from os.path import exists

# constants
ERROR = 255
EMPTY_SUDOKU = [[0] * 9 for x in range(9)]
X_VALUES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
X_VALUES = list(enumerate(X_VALUES))
if sys.stdin.encoding.lower() == "cp850":       # Windows Console
    COLORS = {"clear": "", "bell": "", "yellow": "", "red": ""}
elif sys.stdin.encoding.lower() == "utf-8":     # Unix
    COLORS = {"clear": "\033[0m", \
               "bell": "\a", \
               "grey": "\033[1;30m", \
                "red": "\033[1;31m", \
              "green": "\033[1;32m", \
             "yellow": "\033[1;33m", \
           "darkblue": "\033[1;34m", \
               "pink": "\033[1;35m", \
               "blue": "\033[1;36m"}
elif sys.stdin.encoding.lower() == "cp1252":    # IDLE
    COLORS = {"clear": "", "bell": "", "yellow": "", "red": ""}
else:
    COLORS = {"clear": "", "bell": "", "yellow": "", "red": ""}


# -----
# class implementation
# -----
class Sudoku(object):
    '''Our Sudoku-class.'''
    def __init__(self):
        '''Constructor. Initializes an empty Sudoku.'''
        self.__numbers = EMPTY_SUDOKU

    def enum_column(self, x: str) -> int:
        for i in range(len(X_VALUES)):
            if x in X_VALUES[i]:
                return X_VALUES[i][0]

    def denum_column(self, x: int) -> str:
        for i in range(len(X_VALUES)):
            if x in X_VALUES[i]:
                return X_VALUES[i][1]

    def check_number(self, x: str, y: int, number: int) -> list:
        '''
        Method to check if a newly added number doesnt exist twice in row,
        column or box.
        Returns the positions of all numbers, 
        which conflict with the new number. 
        >>> sud = [[0,4,0,3,0,8,0,1,0],\
                   [2,0,0,4,0,9,0,0,3],\
                   [3,0,5,1,0,2,7,0,4],\
                   [1,0,2,0,0,0,8,0,6],\
                   [0,0,0,0,0,0,0,0,0],\
                   [5,0,9,0,0,0,4,0,7],\
                   [7,0,3,6,0,1,9,0,8],\
                   [8,0,0,7,0,4,0,0,5],\
                   [0,2,0,5,0,3,0,7,0]]
        >>> s = Sudoku()
        >>> s._set_numbers(sud)
        >>> s.check_number('A', 1, 1)
        [('A', 8), ('D', 1)]
        >>> s.check_number('I', 9, 5)
        [('I', 4), ('H', 9)]
        >>> s.check_number('G', 8, 9) # case with a number 9
        [('G', 7)]
        '''
        if (x < 'J') & (y > 0) & (y < 10) & (number > 0) & (number < 10):
            x = self.enum_column(x)
            y -= 1
            row = []
            for i in range(len(self.__numbers)):
                row.append(self.__numbers[i][y])
            box = []
            box_x = []
            box_y = []

            for i in range(3):
                box_x.append(3 * (x // 3) + i)
                box_y.append(3 * (y // 3) + i)

            column_counter = 0
            for v in box_x:
                box.append([])
                for w in box_y:
                    box[column_counter].append(self.__numbers[v][w])
                column_counter += 1

            conflicts = []
            if number in self.__numbers[x]:
                # get y value of all conflicts in the column
                for i in range(len(self.__numbers[x])):
                    if self.__numbers[x][i] == number:
                        conflicts.append((self.denum_column(x), i + 1))
            if number in row:
                # get x value of all conflicts in the row
                for i in range(len(row)):
                    if row[i] == number:
                        conflicts.append((self.denum_column(i), y + 1))

            # get x and y value of all conflicts in the box
            for v in range(len(box)):
                if number in box[v]:
                    for w in range(len(box[v])):
                        if box[v][w] == number:
                            conflicts.append((self.denum_column(box_x[v]), box_y[w] + 1))

            for element in conflicts:
                while conflicts.count(element) > 1:
                    conflicts.remove(element)
                if element == (self.denum_column(x), y + 1):
                    conflicts.remove(element)
            return conflicts
        elif number == 0:
            return []
        else:
            return [ERROR]

    def check(self) -> bool:
        '''
        Method checks the whole Sudoku for conflicts.
        Returns True if Sudoku is correct.
        '''
        correct = True
        if (len(self.__numbers) == 9):
            for x in range(len(self.__numbers)):
                if (len(self.__numbers[x]) == 9) & correct:
                    for y in range(len(self.__numbers[x])):
                        if type(self.__numbers[x][y]) is int:
                            correct = True
                        else:
                            correct = False
                            break
                else:
                    correct = False
                    break
        else:
            correct = False
        if correct:
            for x in range(len(self.__numbers)):
                if correct:
                    for y in range(len(self.__numbers[x])):
                        if self.check_number(self.denum_column(x), y + 1,\
                                self.__numbers[x][y]) == []:
                            correct = True
                        else:
                            correct = False
                            break
                else:
                    break
        return correct

    def get_str(self) -> str:
        '''
        Method to get the Sudoku in a nice printable string.
        Returns the string.
        '''
        nice_str = "      A   B   C     D   E   F     G   H   I\n"
        nice_str += "    _____________ _____________ _____________\n"
        for y in range(9):
            nice_str += "   |             |             |             |\n"
            nice_str += str(y + 1) + "  | "
            for x in range(9):
                nice_str += " "
                if not self.__numbers[x][y] == 0:
                    nice_str += COLORS["yellow"] + str(self.__numbers[x][y]) + COLORS["clear"]
                else:
                    nice_str += "."
                nice_str += "  "
                if x % 3 == 2:
                    nice_str += "| "
            nice_str += "\n"
            if y % 3 == 2:
                nice_str += "   |_____________|_____________|_____________|\n"
        return nice_str

    def get_number(self, x: str, y: int) -> int:
        '''Returns number if coordinates are correct, 255 otherwise'''
        if (x < 'J') & (y > 0) & (y < 10):
            return __numbers[self.enum_column(x)][y - 1]
        else:
            return ERROR

    def get_numbers(self) -> list:
        '''Returns the tuple, which represents the Sudoku'''
        return self.__numbers

    def set_numbers(self, numbers: list):
        ''''''
        self.__numbers = numbers

    def save(self, file_name: str) -> bool:
        '''
        Method to save the Sudoku in a file specified by file_name.
        Returns True if successful.
        '''
        file_name = "saved/" + file_name + ".sudoku"
        if exists(file_name) & (file_name != "saved/.sudoku"):
            print("File already exists.")
            return False
        try:
            f = open(file_name, "wb")
            pickle.dump(self.__numbers, f)
            f.close()
            return True
        except e:
            return False
        
    def load(self, file_name: str) -> bool:
        '''
        Method to load the Sudoku from a save file specified by file_name.
        Returns True if successful.
        '''
        file_name = "saved/" + file_name + ".sudoku"
        try:
            f = open(file_name, "rb")
            self.__numbers = pickle.load(f)
            f.close()
            return True
        except EOFError:
            print("The file you tried to load was corrupted.")
            print("Please do not mess around next time.")
            return False
        except FileNotFoundError:
            print("File doesn't exist.")
            return False
        except e:
            return False
        return True
        
    def add_number(self, x: str, y: int, number: int) -> bool:
        '''
        Method to add a number in the Sudoku. Needs the coordinates x and y
        and the number itself.
        Returns True if successful.
        '''
        if (x < 'J') & (y > 0) & (y < 10):
            self.__numbers[self.enum_column(x)][y - 1] = number
            return True
        else:
            return False

    def del_number(self, x: str, y: int) -> bool:
        '''
        Method to delete a number in the Sudoku.
        Returns True if successful.
        '''
        if (x < 'J') & (y > 0) & (y < 10):
            self.__numbers[self.enum_column(x)][y - 1] = 0
            return True
        else:
            return False

    
        


