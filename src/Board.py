import GameBoard as gb
import Check as c

def run(Gboard):
    print(gb.map)

def BoardCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        run(Gboard)