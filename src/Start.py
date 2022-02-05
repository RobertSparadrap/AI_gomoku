import GameBoard as gb

def check(parsedInput):
    if len(parsedInput) != 2:
        print("ERROR Start command - Invalid arguments.")
        return 84
    try:
        int(parsedInput[1])
    except:
        return 84
    if int(parsedInput[1]) < 5:
        print("ERROR Start command - Invalid size.")
        return 84
    return 0

def run(parsedInput):
    gb.gameBoard_size = int(parsedInput)

def StartCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        run(parsedInput[1])