#!/usr/bin/env python3

from game import *

if __name__ == '__main__':
    game = Game()
    while True:
        moves = game.findMoves()
        if not moves:
            break


