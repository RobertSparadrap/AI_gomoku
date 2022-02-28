#!/usr/bin/env python3

import src.GameBoard as gb
import src.Direction as d
import src.Node as n

def GETVECTOR(direction):
    return d.DIRECTION[direction]

def computeMaximizeWeights(next, maximize, res, player):
    if maximize:
        if maximize == player and next == player:
            res[0] += 10
        else:
            maximize = False
        return maximize, res
    else:
        enemy = 1 if player == 2 else 2
        if not maximize and next == enemy:
            res[1] += 10
        else:
            maximize = True
    return maximize, res

def give_coods(coord, i, dir):
    nx = coord[0] + (GETVECTOR(dir)[0] * i)
    ny = coord[1] + (GETVECTOR(dir)[1] * i)
    if nx not in range(gb.gameBoard_size) or ny not in range(gb.gameBoard_size):
        return -1000, -1000
    return nx, ny

def strikes(direction, coord, enemy, res, nb):
    for dir in direction:
        for i in range(1, 5):
            nx, ny = give_coods(coord, i, dir)
            if nx == ny == -1000:
                continue
            if gb.map[nx][ny] == enemy:
                break
            elif gb.map[nx][ny] == 0:
                res[nb] += 1
                break
    return res

def addStrikes(direction, coord, player, res):
    enemy = 1 if player == 2 else 2
    res = strikes(direction, coord, enemy, res, 0)
    res = strikes(direction, coord, player, res, 1)
    return res