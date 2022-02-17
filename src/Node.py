#!/usr/bin/env python3

import src.GameBoard as gb
import src.Def as d
import src.Win as win

board = None
child = []

def computeMaximizeWeights(next, maximize, res, player):
    if maximize:
        if maximize and next is player:
            res[0] += 10
        else:
            maximize = False
        return maximize, res
    else:
        enemy = d.BRAIN if player is d.OPPONENT else d.OPPONENT
        if not maximize and next is enemy:
            res[1] += 10
        else:
            maximize = True
    return maximize, res

def give_coods(coord, i, dir):
    nx = coord[d.X] + (d.GETVECTOR(dir)[0] * i)
    ny = coord[d.Y] + (d.GETVECTOR(dir)[1] * i)
    if nx not in range(gb.gameBoard_size) or ny not in range(gb.gameBoard_size):
        return -1000, -1000
    return nx, ny

def strikes(direction, coord, enemy, res, nb):
    for dir in direction:
        for i in range(1, d.RANGE+1):
            nx, ny = give_coods(coord, i, dir)
            if nx == ny == -1000:
                continue
            if gb.map[nx][ny] is enemy:
                break
            elif gb.map[nx][ny] is d.EMPTY:
                res[nb] += 1
                break
    return res

def addStrikes(direction, coord, player, res):
    enemy = d.BRAIN if player is d.OPPONENT else d.OPPONENT
    res = strikes(direction, coord, enemy, res, 0)
    res = strikes(direction, coord, player, res, 1)
    return res



def evalDirWeights(direction, res, coord, player, m):
    for dir in direction:
        maxi = m
        for i in range(1, d.RANGE+1):
            nx, ny = give_coods(coord, i, dir)
            if nx == ny == -1000:
                continue
            maxi, res = computeMaximizeWeights(gb.map[nx][ny], maxi, res, player)
    return res


def evalDir(direction, coord, player):
    res = [10, 10]
    res = evalDirWeights(direction, res, coord, player, True)
    res = evalDirWeights(direction, res, coord, player, False)
    res = addStrikes(direction, coord, player, res)
    return res

def ev(i, j, player):
    if win.isWin(gb.map, d.BRAIN):
        return 0
    if win.isWin(gb.map, d.OPPONENT):
        return 10000000000
    ev_SN = evalDir([d.SOUTH, d.NORTH], [i, j], player)
    ev_EW = evalDir([d.EAST, d.WEST], [i, j], player)
    ev_NWS = evalDir([d.NORTHWEST, d.SOUTHEAST], [i, j], player)
    ev_NES = evalDir([d.NORTHEAST, d.SOUTHWEST], [i, j], player)
    eval = [ev_SN, ev_EW, ev_NWS, ev_NES]
    transpose = list(map(list, zip(*eval)))
    return max(max(res for res in transpose))

def loop(board, depth, player, ch=None):
    global child
    if depth == 0:
        return
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is d.EMPTY:
                board[i][j] = player
                score = ev(i, j, player)
                child.append([board, i, j, score])
                nextPlayer = d.BRAIN if player is d.OPPONENT else d.OPPONENT
                loop(board, depth-1, nextPlayer, child[-1])
                board[i][j] = d.EMPTY

def run(Gboard, depth, player):
    global board
    board = gb.copy(Gboard)
    loop(board, depth, player)
    return