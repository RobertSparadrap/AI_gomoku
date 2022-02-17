#!/usr/bin/env python3

import src.GameBoard as gb
import src.Def as d
import src.Check as c
import src.IA as ia

def check(parsedInput):
    if c.checkFun(parsedInput, 3) == 84:
        return 84
    try:
        x = int(parsedInput[1])
        y = int(parsedInput[2])
    except:
        print("ERROR, Turn command - Invalid size.")
        return 84
    if x not in range(gb.gameBoard_size) or y not in range(gb.gameBoard_size):
        return 84
    if gb.map[x][y] == 1:
        return 84
    return 0

def runPlayer(parsedInput, Gboard):
    x = int(parsedInput[1])
    y = int(parsedInput[2])
    gb.map[x][y] = d.OPPONENT

def runAI(Gboard):
    x_ia, y_ia = ia.run(Gboard)
    print(x_ia, y_ia)
    gb.map[x_ia][y_ia] = d.BRAIN

def TurnCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        runPlayer(parsedInput, Gboard)
        runAI(Gboard)