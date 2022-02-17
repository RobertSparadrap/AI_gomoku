#!/usr/bin/env python3

import src.Def as d
import src.Node as n

def minimax(gameBoard, depth, cc, player):
    bestMove = [-1, -1, 0]
    if depth == 0 or len(cc) == 0:
       return cc[1], cc[2], cc[3]
    for c in cc:
        move = minimax(gameBoard, depth-1, c, d.NEXTPLAYER(player))
        if (player is d.BRAIN and move[2] > bestMove[2]) or (player is not d.BRAIN and move[2] < bestMove[2]):
            bestMove = move
    return bestMove

def run(map):
    depth = 1
    n.run(map, depth, d.BRAIN)
    x, y, _ = minimax(map, depth, n.child, d.BRAIN)
    return x, y
