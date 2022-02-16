#!/usr/bin/env python3

import src.GameBoard as gb
import src.Check as c

def run(Gboard):
    print(gb.map)

def BoardCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        run(Gboard)