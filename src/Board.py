import GameBoard as gb

def check(parsedInput):
    if len(parsedInput) != 1:
        print("ERROR Board command - No arguments expected.")
        return 84
    return 0

def run(Gboard):
    print(gb.create(19))

def BoardCmd(parsedInput, Gboard):
    if check(parsedInput) != 84:
        run(Gboard)