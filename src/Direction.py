#!/usr/bin/env python3

NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7

DIRECTION = [
    [-1, 0],    # NORTH
    [-1, 1],    # NORTHEAST
    [0, 1],     # EAST
    [1, 1],     # SOUTHEAST
    [1, 0],     # SOUTH
    [1, -1],    # SOUTHWEST
    [0, -1],    # WEST
    [-1, -1]    # NORTHWEST
]
