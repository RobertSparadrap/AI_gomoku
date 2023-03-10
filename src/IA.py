#!/usr/bin/env python3

import src.Direction as d
import src.Node as n
import src.GameBoard as gb

def NEXTPLAYER(player):
    return 1 if player == 2 else 2

def minimax(gameBoard, depth, cc, player):
    bestMove = [-1, -1, 0]
    if depth == 0 or len(cc) == 0:
       return cc[1], cc[2], cc[3]
    for c in cc:
        move = minimax(gameBoard, depth-1, c, NEXTPLAYER(player))
        if (player == 1 and move[2] > bestMove[2]) or (player != 1 and move[2] < bestMove[2]):
            if gb.map[move[0]][move[1]] == 0:
                bestMove = move
            print(gb.map[move[0]][move[1]])
    return bestMove

def run(map):
    depth = 1
    n.run(map, depth, 1)
    x, y, _ = minimax(map, depth, n.child, 1)
    return x, y
