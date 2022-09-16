#!/usr/bin/env python3

from game import Game

charToColor = {'W': 'White', 'B': 'Black'}

if __name__ == '__main__':
    game = Game()
    f = open("./lastgame.txt", "w")
    moveNum = 1
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
                if game.ToMove == 'B':
                    #TODO: get proper move format out of MakeMove
                    f.write(str(moveNum) + ". " + selectedMove)
                else:
                    f.write(" " + selectedMove + "\n")
                    moveNum += 1
                break
            else:
                print("Invalid move.")

