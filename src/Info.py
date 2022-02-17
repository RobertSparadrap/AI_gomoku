#!/usr/bin/env python3

import src.GameBoard as gb
import src.Check as c

def check(parsedInput, settings):
    if c.checkFun(parsedInput, 3) == 84:
        return 84
    if parsedInput[1] not in settings.keys():
        print("ERROR, Info command - Invalid key.")
        return 84
    return 0

def InfoCmd(parsedInput, Gboard):
    if check(parsedInput, gb.settings) != 84:
        key = parsedInput[1]
        value = parsedInput[2]
        gb.settings[key] = int(value)