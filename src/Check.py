#!/usr/bin/env python3

def checkFun(parsedInput, n):
    if len(parsedInput) != n:
        print("ERROR, Turn command - Invalid arguments.", flush=True)
        return 84
    return 0