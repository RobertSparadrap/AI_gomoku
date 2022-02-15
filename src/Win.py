import GameBoard as gb

def x_axis(nb_y, nb_i, map, player):
    score = 1
    for i in range(1, 5):
        if nb_i + i > gb.gameBoard_size - 1:
            return score
        if map[nb_y][nb_i + i] == player:
            score += 1
    return score

def y_axis(nb_y, nb_i, map, player):
    score = 1
    for i in range(1, 5):
        if nb_y + i > gb.gameBoard_size -1:
            return score
        if map[nb_y + i][nb_i] == player:
            score += 1
    return score

def diagOne(nb_y, nb_i, map, player):
    score = 1
    for i in range(1, 5):
        if nb_y + i > gb.gameBoard_size - 1 or nb_i + i > gb.gameBoard_size - 1:
            return score
        if map[nb_y + i][nb_i + i] == player:
            score += 1
    return score

def diagTwo(nb_y, nb_i, map, player):
    score = 1
    for i in range(1, 5):
        if nb_y + i > gb.gameBoard_size - 1:
            return score
        if map[nb_y + i][nb_i - i] == player:
            score += 1
    return score

def checkWin(nb_y, nb_i, find, map, player):
    score = 1
    if find == player:
        if x_axis(nb_y, nb_i, map, player) == 5:
            return 5
        if y_axis(nb_y, nb_i, map, player) == 5:
            return 5
        if diagOne(nb_y, nb_i, map, player) == 5:
            return 5
        if diagTwo(nb_y, nb_i, map, player) == 5:
            return 5
    return score


def isWin(map, player):
    nb_y = 0
    nb_i = 0
    for y in range(0, gb.gameBoard_size):
        for i in range(0, gb.gameBoard_size):
            if checkWin(y, i, map[y][i], map, player) == 5:
                return 1
            nb_i += 1
        nb_y += 1
    return 0