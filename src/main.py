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

def printMap():
    print(end=" ")
    for i in range(1, 21):
        print(chr(i + 64), end= " ")
    print()
    for i in range(165):
        print("_", end="")
    print()
    j = 0
    for i in range(20):
        j = 0
        print("%d|\t" %(i), end="")
        for j in range(20):
            print(gb.map[i][j], end=" ")
        print()
    print()

def startParse():
    line = ""
    while(line != "END"):
#        line = sys.stdin.readline()
        try:
            line = input()
        except:
            exit(0)
#        if not line:
#            break
        if not line:
            break
        if line == '':
            pars_inpt = ['UNKNOWN']
        else:
            pars_inpt = line.strip().split(" ")
        if pars_inpt[0] in COMMANDS:
            COMMANDS[pars_inpt[0]](pars_inpt, gb.map)
#            printMap()
        else:
            print("Error Command", flush=True)

def main():
    startParse()

#try:
if __name__ == "__main__":
	 main()
#except:
#    exit(84)