import sys

import GameBoard as gb
import Start as start
#import src.commands.Turn
#import src.commands.Begin
import Board as board
import Info as info
import EndProg as end
import About as about

COMMANDS = {
            'START': start.StartCmd,
#            'TURN': TurnCmd,
#            'BEGIN': BeginCmd,
            'BOARD': board.BoardCmd,
            'INFO': info.InfoCmd,
            'END': end.EndCmd,
            'ABOUT': about.AboutCmd
        }

def startParse(pars_inpt):
    if pars_inpt[0] in COMMANDS:
        COMMANDS[pars_inpt[0]](pars_inpt, gb.create(gb.gameBoard_size))
    else:
        print("Error Command")
        exit(84)

def game():
    while(1):
        line = sys.stdin.readline()
        if line == '':
            pars_inpt = ['UNKNOWN']
        else:
            pars_inpt = line.strip().split(" ")
#        print(pars_inpt)
        startParse(pars_inpt)

def main():
    game()

if __name__ == "__main__":
	main()