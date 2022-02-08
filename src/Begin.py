import GameBoard as gb
import Def as d
import Check as c

def run(Gboard):
    x = int(gb.gameBoard_size/2)
    y = int(gb.gameBoard_size/2)
    print(x, y)
    gb.map[x][y] = d.BRAIN

def BeginCmd(parsedInput, Gboard):
    if c.checkFun(parsedInput, 1) != 84:
        run(Gboard)