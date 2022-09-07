#!/usr/bin/env python3

fileITA = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
rankITA = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
fileATI = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
rankATI = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

pawnChar = 'p'
knightChar = 'N'
bishopChar = 'B'
rookChar = 'R'
queenChar = 'Q'
kingChar = 'K'
whiteChar = 'W'
blackChar = 'B'
emptySquare = "  "
captureChar = 'x'

class Game:

    #Creates an instance of the Game class. Sets up the board and initiates White as the starting player
    def __init__(self):
        self.ToMove = "W"
        self.Board = self.makeBoard()
        self.enPassantSquare = ""

    #Sets up the chessboard for a new game
        #returns: list of 8 lists, each representing a rank in a chessboard and containing 8 2-character strings
    def makeBoard(self):
        EmptyRow = [emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare]
        BlackBackRow = self.makeBackRow(blackChar)
        BlackFrontRow = self.makeFrontRow(blackChar)
        WhiteFrontRow = self.makeFrontRow(whiteChar)
        WhiteBackRow = self.makeBackRow(whiteChar)
        return [WhiteBackRow, WhiteFrontRow, EmptyRow, EmptyRow, EmptyRow, EmptyRow, BlackFrontRow, BlackBackRow]

    #Sets up the back row for one color
        #param color: 'W' or 'B'
        #returns: list of 8 2-character strings representing the starting back rank for one color
    def makeBackRow(self, color):
        return [color + rookChar, color + knightChar, color + bishopChar, color + queenChar, color + kingChar, color + bishopChar, color + knightChar, color + rookChar]

    #Sets up the front row for one color
        #param color: 'W' or 'B'
        #returns: list of 8 2-character strings representing the starting front rank for one color
    def makeFrontRow(self, color):
        return [color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar]

    #Prints the current state of the chessboard (from White's perspective)
    def printBoard(self):
        for row in reversed(self.Board):
            print(row)

    #Finds all moves for the player who has the next move
        #returns: list of moves that the player can make. e4, exd4, Nf3, O-O-O, etc.
    def findMoves(self):
        moves = []
        for rankIndex, rank in enumerate(self.Board):
            for fileIndex, square in enumerate(rank):
                if square[0] != self.ToMove:
                    continue
                if square[1] == pawnChar:
                    moves.extend(self.findPawnMoves(rankIndex, fileIndex))
                    #TODO: other pieces
        return moves

    #Gets direction that a particular pawn on the board is moving
        #param rankIndex: rank the pawn is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the pawn is on. 0 = a-file, 1 = b-file, etc.
        #returns direction: 1 for White and pawn is moving forward, -1 for Black and pawn is moving backward
        #returns startRank: 1 for White, 6 for Black
    def getPawnDirection(self, rankIndex, fileIndex):
        if self.Board[rankIndex][fileIndex][0] == whiteChar:
            startRank = 1
            direction = 1
        elif self.Board[rankIndex][fileIndex][0] == blackChar:
            startRank = 6
            direction = -1
        else:
            raise Exception("No piece here")
        return direction, startRank


    #Finds moves a particular pawn can make
        #param rankIndex: rank the pawn is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the pawn is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the pawn can make. e3, e4, exd4, e8=Q, etc.
        #TODO: promotion
        #TODO: capturing
    def findPawnMoves(self, rankIndex, fileIndex):
        moves = []
        if self.Board[rankIndex][fileIndex][0] != self.ToMove:
            raise Exception("Looking for the wrong color")
        if rankIndex <= 0 or rankIndex >= 7:
            raise Exception("Pawn in the wrong place")
        direction, startRank = self.getPawnDirection(rankIndex, fileIndex)
        #TODO: check for check
        if self.Board[rankIndex + direction][fileIndex] == emptySquare:
            moves.append(fileITA[fileIndex] + rankITA[rankIndex + direction])
            if rankIndex == startRank and self.Board[rankIndex + direction + direction][fileIndex] == emptySquare:
                moves.append(fileITA[fileIndex] + rankITA[rankIndex + direction + direction])

        return moves 
    
    #Accepts a move and makes it on the chessboard
        #param move: a legal chess move that can be taken by the active player. e3, exd4, Nf3, O-O-O, etc.
    def MakeMove(self, move):
        #figure out which piece type is moving
        if move[0] in fileITA.values():
            makePawnMove(move)
        #TODO: other pieces

    #Accepts a pawn move and makes it on the chessboard
        #param move: a legal pawn move that can be taken by the active player. e3, exd4, e8=Q, etc.
    def makePawnMove(self, move):
        if 'x' in move:
            targetFileIndex = fileATI[move[2]]
            sourceFileIndex = fileATI[move[0]]
            targetRankIndex = rankATI[move[3]]
            sourceRankIndex = fileATI[move[
        else:
            targetFileIndex = fileATI[move[0]]
            sourceFileIndex = fileATI[move[0]]
            targetRankIndex = rankATI[move[1]]
            










