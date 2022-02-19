#!/usr/bin/env python3

import src.GameBoard as gb
import src.Check as c
import src.Turn as play
import sys

def BoardCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        while 1:
            line = input()
#            line = sys.stdin.readline()
            if line == '':
                pars_inpt = ['UNKNOWN']
            else:
                pars_inpt = line.strip().split(",")
            try:
                pars_inpt[0] = int(pars_inpt[0]) - 1
                pars_inpt[1] = int(pars_inpt[1]) - 1
                pars_inpt[2] = int(pars_inpt[2])
#                print(pars_inpt[2])
            except:
                if pars_inpt[0] == "DONE":
                    play.runAI(gb.map)
                    break
#            print(pars_inpt)
            if pars_inpt[2] == 1 or pars_inpt[2] == 2:
                gb.map[pars_inpt[0]][pars_inpt[1]] = pars_inpt[2]
            else:
                print("ERROR")
#        print(gb.map)