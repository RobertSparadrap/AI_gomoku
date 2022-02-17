#!/usr/bin/env python3

import src.GameBoard as gb
import src.Check as c

def BoardCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        print(gb.map)