import GameBoard as gb
import Def as d
import Check as c

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

def run(parsedInput):
    x = int(parsedInput[1])
    y = int(parsedInput[2])
    gb.map[x][y] = d.OPPONENT

def TurnCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        run(parsedInput)