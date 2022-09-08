#!/usr/bin/env python3

from game import Game

charToColor = {'W': 'White', 'B': 'Black'}

if __name__ == '__main__':
    game = Game()
    while True:
        print()
        print("It's " + charToColor[game.ToMove] + "'s move!")
        game.printBoard()
        moves = game.findMoves()
        if not moves:
            break
        print()
        print(charToColor[game.ToMove] + "'s possible moves:")
        print(moves)
        print()
        while True:
            selectedMove = input("Select a move: ")
            #TODO: undo
            if selectedMove in moves:
                game.MakeMove(selectedMove)
                break
            else:
                print("Invalid move.")
            #TODO: save moves to a file

