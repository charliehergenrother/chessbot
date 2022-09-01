#!/usr/bin/env python3

class Game:
    pawnChar = 'p'
    knightChar = 'N'
    bishopChar = 'B'
    rookChar = 'R'
    queenChar = 'Q'
    kingChar = 'K'
    whiteChar = 'W'
    blackChar = 'B'
    emptySquare = "  "
    fileTranslation = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

    def __init__(self):
        self.ToMove = "W"
        self.Board = self.makeBoard()
        self.printBoard()
        self.enPassantSquare = ""

    def makeBoard(self):
        EmptyRow = [emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare]
        BlackBackRow = self.makeBackRow(blackChar)
        BlackFrontRow = self.makeFrontRow(blackChar)
        WhiteFrontRow = self.makeFrontRow(whiteChar)
        WhiteBackRow = self.makeBackRow(whiteChar)
        board = [WhiteBackRow, WhiteFrontRow, EmptyRow, EmptyRow, EmptyRow, EmptyRow, BlackFrontRow, BlackBackRow]
        return board

    def makeBackRow(self, color):
        return [color + rookChar, color + knightChar, color + bishopChar, color + queenChar, color + kingChar, color + bishopChar, color + knightChar, color + rookChar]

    def makeFrontRow(self, color):
        return [color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar, color + pawnChar]

    def printBoard(self):
        for row in reversed(self.board):
            print(row)

    def findMoves(self):
        moves = []
        for rankIndex, rank in enumerate(self.Board):
            for fileIndex, square in rank:
                if square[0] != self.ToMove:
                    continue
                if square[1] == pawnChar
                    moves.append(self.findPawnMoves(rankIndex, fileIndex))
        return moves

    def findPawnMoves(self, rankIndex, fileIndex)
        moves = []
        if self.Board[rankIndex][fileIndex][0] != self.ToMove:
            raise Exception("Looking for the wrong color")
        if rankIndex <= 0 or rankIndex >= 7:
            raise Exception("Pawn in the wrong place")
        if self.Board[rankIndex][fileIndex][0] == self.whiteChar:
            startRank = 1
            direction = 1
        else if self.Board[rankIndex][fileIndex][0] == self.blackChar:
            startRank = 6
            direction = -1
        else:
            raise Exception("No piece here")
        if self.Board[rankIndex + direction][fileIndex] = self.emptyChar:
            moves.append(


        return moves 












