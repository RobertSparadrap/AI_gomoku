#!/usr/bin/env python3

# POINTS
X = 0
Y = 1
SCORE = 2

# CELL TYPES
EMPTY = 0
BRAIN = 1
OPPONENT = 2

# MOVE TYPES
ATTACK = 0
DEFENSE = 1

# DIRECTIONS
NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7

VECTOR = [
    [-1, 0],    # NORTH
    [-1, 1],    # NORTHEAST
    [0, 1],     # EAST
    [1, 1],     # SOUTHEAST
    [1, 0],     # SOUTH
    [1, -1],    # SOUTHWEST
    [0, -1],    # WEST
    [-1, -1]    # NORTHWEST
]

RANGE = 4

def GETVECTOR(direction):
    return VECTOR[direction]
    
def NEXTPLAYER(player):
    return BRAIN if player is OPPONENT else OPPONENT