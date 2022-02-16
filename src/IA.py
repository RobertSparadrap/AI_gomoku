#!/usr/bin/env python3

import src.Def as d
import src.Node as n

#def minimax(gameBoard, depth, node, player):
#    if depth == 0 or len(node._children) == 0:
#        return node._coords
#    if player is d.BRAIN:
#        bestMove = [-1, -1, -inf]
#        for child in node._children:
#            move = minimax(gameBoard, depth-1, child, d.NEXTPLAYER(player))
#            if move[d.SCORE] > bestMove[d.SCORE]:
#                bestMove = deepcopy(move)
#    else:
#        bestMove = [-1, -1, inf]
#        for child in node._children:
#            move = minimax(gameBoard, depth-1, child, d.NEXTPLAYER(player))
#            if move[d.SCORE] < bestMove[d.SCORE]:
#                bestMove = deepcopy(move)
#    return bestMove

def run(map):
    depth = 1
    n.run(map, depth, d.BRAIN)
    return 0, 0
#    tree = Tree(map, depth, d.BRAIN)
#    x, y, _ = minimax(map, depth, tree._root, d.BRAIN)
#    return x, y