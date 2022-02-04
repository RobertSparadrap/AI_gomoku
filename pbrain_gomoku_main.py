import sys

MIN_BOARD = 5
MAX_BOARD = 100
COMMANDS = [ "START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT" ]
FUNCTIONS_STR = [ "startCmd", "turnCmd", "beginCmd", "boardCmd", "infoCmd", "endCmd", "aboutCmd" ]

boardSize = 0
gameBoard = None

def startCmd(size):
    global boardSize
    global gameBoard

    size = int(size)
    if size < MIN_BOARD or size > MAX_BOARD:
        sys.exit(84)
    boardSize = size
    gameBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
    print("Ok")
    sys.stdout.flush()


def turnCmd(pos, unused):
    global gameBoard
    global boardSize

    posTab = pos.split(",")
    gameBoard[int(posTab[1])][int(posTab[0])] = 2

    pos = ai.chooseNextMove(gameBoard)
    gameBoard[pos[0]][pos[1]] = 1
    print("{},{}".format(pos[1], pos[0]))
    sys.stdout.flush()

def beginCmd(unused, unused2):
    global gameBoard
    global boardSize

    pos = ai.chooseNextMove(gameBoard)
    gameBoard[pos[0]][pos[1]] = 1
    print("{},{}".format(pos[1], pos[0]))
    sys.stdout.flush()

def boardCmd(unused, unused2):
    global gameBoard
    global boardSize

    line = sys.stdin.readline()
    commandTab = line.strip().split(" ")
    while commandTab[0] != "DONE":
        pos = line.strip().split(",")
        gameBoard[pos[1]][pos[0]] = pos[2]
        line = sys.stdin.readline()
        commandTab = line.strip().split(" ")

    posX, posY = misc.choosePosition(gameBoard)
    gameBoard[posY][posX] = 1
    print("{},{}".format(posX, posY))
    sys.stdout.flush()

def infoCmd(key, value):
    pass

def endCmd(unused, unused2):
    exit(0)

def aboutCmd(unused, unused2):
    print("Gomoku")
    sys.stdout.flush()


def main():
    while True:
        line = sys.stdin.readline()
        commandTab = line.strip().split(" ")
        if commandTab[0] in COMMANDS:
            if len(commandTab) > 1:
                param1 = commandTab[1]
            else:
                param1 = 0
            if len(commandTab) > 2:
                param2 = commandTab[2]
            else:
                param2 = 0
            if commandTab[0] == "START":
                startCmd(param1)
        else:
            print("Error")
            sys.stdout.flush()


if __name__ == "__main__":
	main()