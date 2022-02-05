import sys

import GameBoard as gb
#import src.commands.Start
#import src.commands.Turn
#import src.commands.Begin
#import src.commands.Board
#import src.commands.Info
#import src.commands.End
#import src.commands.About
#import src.utils.Log

#COMMANDS = {
#            'START': StartCmd,
#            'TURN': TurnCmd,
#            'BEGIN': BeginCmd,
#            'BOARD': BoardCmd,
#            'INFO': InfoCmd,
#            'END': EndCmd,
#            'ABOUT': AboutCmd
#        }
#gameBoard = gb.GameBoard(19)

def start(pars_inpt):
    try:
        print(gb.create(19))
#        COMMANDS[pars_inpt[0]](pars_inpt, gameBoard)
    except:
        print("Error")
        exit(84)

def game():
    while(1):
        line = sys.stdin.readline()
        if line == '':
            pars_inpt = ['UNKNOWN']
        else:
            pars_inpt = line.strip().split(" ")
        print(pars_inpt)
        start(pars_inpt)

def main():
    game()

if __name__ == "__main__":
	main()