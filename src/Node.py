#!/usr/bin/env python3

import src.GameBoard as gb
import src.Direction as d
import src.EvalWeights as eval
import src.EvalCoord as coord

board = None
child = []


def loop(board, depth, player, ch=None):
    global child
    if depth == 0:
        return
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                board[i][j] = player
                score = eval.ev(i, j, player)
                child.append([board, i, j, score])
                nextPlayer = 1 if player == 2 else 2
                loop(board, depth-1, nextPlayer, child[-1])
                board[i][j] = 0

def run(Gboard, depth, player):
    global board
    board = gb.copy(Gboard)
    loop(board, depth, player)
    return