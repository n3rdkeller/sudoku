------------------------
         SUDOKU
------------------------
       README.TXT
------------------------

------------------------
        GENERAL
      INFORMATION
------------------------

The main program of our sudoku-program
is in the file "main.py".

There is an example-sudoku in the
subdirectory "saved". How to load 
that one is explained later.

Your games are saved in the subdirectory
"saved". They do all have the extension
".sudoku". They are saved in a binary
way and should not be changed manually.
(Because this would cause an error in python.)


------------------------
      INSTRUCTIONS
------------------------

When you start the program you will see
an empty sudoku and a prompt that is
asking for a command.

Now you are able to type one of the 
commands from the "commands" section
to "interact" with your sudoku.

The syntax of every command is NOT case-
sensitive except the optional filename.

To see the following descriptions
in the program, just type
"help" or "help {command}".


------------------------
       COMMANDS
------------------------

HELP        displays a help
ADD         adds a number
DEL         deletes a number
SAVE        saves the sudoku
LOAD        loads a sudoku
CHK         checks the whole sudoku
QUIT        quits the game
NEW         creates empty sudoku


ADD (A-I)(1-9) (1-9)
Adds a number to a position specified by
alphanumeric coordinates.
examples: 'ADD B3 6', 'ADD E5 3'

DEL (A-I)(1-9)
Deletes position specified by
alphanumeric coordinates.
examples: 'DEL B3','DEL E5'

SAVE {filename}
Saves the current sudoku to the given filename.
If empty, the sudoku is saved into
the default file ".sudoku"
example: 'SAVE my_sudoku'

LOAD {filename}
Loads a saved sudoku.
If empty, the default file ".sudoku" is loaded.
example: 'LOAD my_sudoku'

CHK
Checks the whole sudoku for errors.

QUIT
Quits the game.

NEW
Creates empty sudoku without (!)
saving the current.


------------------------
        CREDITS
------------------------

Thank you so much, we love you too.


------------------------
   PLANNED FEATURES
------------------------

We have planned to add some features in the future.
Some of these are:
- fixed fields (for the example-files)
- solver (to get hints)
- hints ;)
- list to show all savegames
- possibility to remove savegames