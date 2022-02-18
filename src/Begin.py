#!/usr/bin/env python3

import src.GameBoard as gb
import src.Def as d
import src.Check as c

def run(Gboard):
    x = int(gb.gameBoard_size/2)
    y = int(gb.gameBoard_size/2)
    print("%d,%d" %(x, y))
    gb.map[x][y] = d.BRAIN

def BeginCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        run(Gboard)