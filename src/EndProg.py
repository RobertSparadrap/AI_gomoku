#!/usr/bin/env python3

import src.Check as c

def check(parsedInput):
    if len(parsedInput) != 1:
        print("ERROR Board command - No arguments expected.", flush=True)
        return 84
    return 0

def EndCmd(parsedInput, unused):
    if c.checkFun(parsedInput, 1) != 84:
        print("Programme ended", flush=True)
#        exit(0)