import GameBoard as gb

coordonee = [-1, -1, 0]
board = None

def run(Gboard):
    global board
    board = gb.copy(Gboard)
    board[0][0] = "CHEH"
    return