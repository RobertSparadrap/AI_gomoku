#!/usr/bin/env python3

import src.GameBoard as gb
import src.Direction as d
import src.Check as c

def run(Gboard):
    x = int(gb.gameBoard_size/2)
    y = int(gb.gameBoard_size/2)
#    print("%d,%d" %(x + 1, y + 1), flush=True)
    print("%d,%d" %(x, y), flush=True)
    gb.map[x][y] = 1
#    print(gb.map)

def BeginCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        run(Gboard)