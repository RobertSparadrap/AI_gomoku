import GameBoard as gb
import Def as d

def check(parsedInput):
    if len(parsedInput) != 1:
        print("ERROR Begin command - No arguments expected.")
        return 84
    return 0

def run(Gboard):
    x = int(gb.gameBoard_size/2)
    y = int(gb.gameBoard_size/2)
    print(x, y)
    gb.map[x][y] = d.BRAIN

def BeginCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        run(Gboard)