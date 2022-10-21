#!/usr/bin/env python3

from game import Game
import sys

charToColor = {'W': 'White', 'B': 'Black'}

def getMove():
    try:
        selectedMove = input("Select a move: ")
    except EOFError:
        print()
        sys.exit()
    return selectedMove

def processMove(selectedMove, moves, game, f):
    if selectedMove in moves:
        game.MakeMove(selectedMove)
        if game.ToMove == 'B':
            #TODO: get proper move format out of MakeMove
            f.write(str(game.MoveNum) + ". " + selectedMove)
        else:
            f.write(" " + selectedMove + "\n")
            game.MoveNum += 1
        return False
    else:
        print("Invalid move.")

def printHelp():
    print('Welcome to chessbot!')
    print('To run:')
    print('./rungame.py [-h] [-f <input file>]')
    sys.exit()

def processArgs():
    argIndex = 1
    f = ""
    while argIndex < len(sys.argv):
        if sys.argv[argIndex] == '-f':
            f = sys.argv[argIndex+1]
            if "lastgame.txt" in f:
                print("can't use that! I'm going to record the moves there!")
                sys.exit()
        elif sys.argv[argIndex] == '-h':
            printHelp()
        argIndex += 1
    return f

if __name__ == '__main__':
    inputFile = processArgs()
    game = Game()
    f = open("./lastgame.txt", "w")
    if inputFile:
        i = open(inputFile, "r")
        for line in i:
            madeMoves = line.strip().split(' ')
            possibleMoves = game.findMoves()
            processMove(madeMoves[1], possibleMoves, game, f) 
            possibleMoves = game.findMoves()
            try:
                processMove(madeMoves[2], possibleMoves, game, f) 
            except IndexError:
                break
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
            selectedMove = getMove()
            #TODO: undo
            if not processMove(selectedMove, moves, game, f):
                break
