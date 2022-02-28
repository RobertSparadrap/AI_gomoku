#!/usr/bin/env python3

import src.GameBoard as gb
import src.Check as c

def check(parsedInput):
    if c.checkFun(parsedInput, 2) == 84:
        return 84
    try:
        int(parsedInput[1])
    except:
        return 84
    if int(parsedInput[1]) < 5:
        print("ERROR Start command - Invalid size.", flush=True)
        return 84
    return 0

def StartCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        gb.gameBoard_size = int(parsedInput[1])
        gb.map = gb.create(gb.gameBoard_size)
        print("Ok", flush=True)