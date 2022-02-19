#!/usr/bin/env python3

import src.GameBoard as gb
import src.Direction as d
import src.Win as win
import src.Node as n
import src.EvalCoord as crd

def evalDirWeights(direction, res, coord, player, m):
    for dir in direction:
        maxi = m
        for i in range(1, 5):
            nx, ny = crd.give_coods(coord, i, dir)
            if nx == ny == -1000:
                continue
            maxi, res = crd.computeMaximizeWeights(gb.map[nx][ny], maxi, res, player)
    return res


def evalDir(direction, coord, player):
    res = [10, 10]
    res = evalDirWeights(direction, res, coord, player, True)
    res = evalDirWeights(direction, res, coord, player, False)
    res = crd.addStrikes(direction, coord, player, res)
    return res

def ev(i, j, player):
    if win.isWin(gb.map, 1):
        return 0
    if win.isWin(gb.map, 2):
        return 10000000000
    ev_SN = evalDir([d.SOUTH, d.NORTH], [i, j], player)
    ev_EW = evalDir([d.EAST, d.WEST], [i, j], player)
    ev_NWS = evalDir([d.NORTHWEST, d.SOUTHEAST], [i, j], player)
    ev_NES = evalDir([d.NORTHEAST, d.SOUTHWEST], [i, j], player)
    eval = [ev_SN, ev_EW, ev_NWS, ev_NES]
    transpose = list(map(list, zip(*eval)))
    return max(max(res for res in transpose))