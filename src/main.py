#!/usr/bin/env python3
import sys

import src.GameBoard as gb
import src.Start as start
import src.Turn as turn
import src.Begin as begin
import src.Board as board
import src.Info as info
import src.EndProg as end
import src.About as about

COMMANDS = {
            'START': start.StartCmd,
            'TURN': turn.TurnCmd,
            'BEGIN': begin.BeginCmd,
            'BOARD': board.BoardCmd,
            'INFO': info.InfoCmd,
            'END': end.EndCmd,
            'ABOUT': about.AboutCmd
        }

def startParse(pars_inpt):
    if pars_inpt[0] in COMMANDS:
        COMMANDS[pars_inpt[0]](pars_inpt, gb.map)
    else:
        print("Error Command")

def game():
    while(1):
        line = sys.stdin.readline()
        if line == '':
            pars_inpt = ['UNKNOWN']
        else:
            pars_inpt = line.strip().split(" ")
        startParse(pars_inpt)

def main():
    game()

if __name__ == "__main__":
	main()