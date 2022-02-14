import GameBoard as gb
import Def as d
import Win as win
from math import inf

coordonee = [-1, -1, 0]
board = None
child = []

def evalDir(direction, coord, player):
    return 0

def ev(i, j, player):
    if win.isWin(board, d.BRAIN):
        return inf
    if win.isWin(board, d.OPPONENT):
        return 10000000000
    ev_SN = evalDir([d.SOUTH, d.NORTH], [i, j], player)
    ev_EW = evalDir([d.EAST, d.WEST], [i, j], player)
    ev_NWS = evalDir([d.NORTHWEST, d.SOUTHEAST], [i, j], player)
    ev_NES = evalDir([d.NORTHEAST, d.SOUTHWEST], [i, j], player)
    eval = [ev_SN, ev_EW, ev_NWS, ev_NES]
    transpose = list(map(list, zip(*eval)))
    return max(max(res for res in transpose))

def loop(board, depth, player):
    if depth == 0:
        return
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is d.EMPTY:
                board[i][j] = player
                score = ev(i, j, player)
                nextPlayer = d.BRAIN if player is d.OPPONENT else d.OPPONENT
                loop(board, depth-1, nextPlayer)
                board[i][j] = d.EMPTY

def run(Gboard, depth, player):
    global board
    board = gb.copy(Gboard)
    loop(board, depth, player)
    return