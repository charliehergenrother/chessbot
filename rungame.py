#!/usr/bin/env python3

from game import Game

charToColor = {'W': 'White', 'B': 'Black'}

if __name__ == '__main__':
    game = Game()
    while True:
        print("It's " + charToColor[game.ToMove] + "'s move!")
        game.printBoard()
        moves = game.findMoves()
        if not moves:
            break
        print(charToColor[game.ToMove] + "'s possible moves:")
        print(moves)
        while True:
            selectedMove = input("Select a move:")
            if selectedMove in moves:
                pass
                # game.MakeMove(selectedMove)
            else:
                print("Invalid move.")

