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
opponent = {'W': 'B', 'B': 'W'}

#Class containing all information for a running chess game
class Game:

    #Creates an instance of the Game class. Sets up the board and initiates White as the starting player
    def __init__(self):
        self.ToMove = whiteChar
        self.Board = self.makeBoard()
        self.enPassantSquare = ""
        self.MoveNum = 1

    #Sets up the chessboard for a new game
        #returns: list of 8 lists, each representing a rank in a chessboard and containing 8 2-character strings
    def makeBoard(self):
        EmptyRow = [emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare, emptySquare]
        BlackBackRow = self.makeBackRow(blackChar)
        BlackFrontRow = self.makeFrontRow(blackChar)
        WhiteFrontRow = self.makeFrontRow(whiteChar)
        WhiteBackRow = self.makeBackRow(whiteChar)
        return [WhiteBackRow, WhiteFrontRow, list(EmptyRow), list(EmptyRow), list(EmptyRow), list(EmptyRow), BlackFrontRow, BlackBackRow]

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
                elif square[1] == knightChar:
                    moves.extend(self.findKnightMoves(rankIndex, fileIndex))
                elif square[1] == bishopChar:
                    moves.extend(self.findBishopMoves(rankIndex, fileIndex))
                elif square[1] == rookChar:
                    moves.extend(self.findRookMoves(rankIndex, fileIndex))
                elif square[1] == queenChar:
                    moves.extend(self.findQueenMoves(rankIndex, fileIndex))
                elif square[1] == kingChar:
                    moves.extend(self.findKingMoves(rankIndex, fileIndex))
                #TODO: castling
        return sorted(moves)
    
    #Gets the direction the active player is going on the chessboard
        #returns 1 if the active player is White and -1 if it is Black
    def getColorDirection(self):
        if self.ToMove == whiteChar:
            return 1
        else:
            return -1
    
    #Gets the starting rank index of the pawns for the active player
        #returns 1 if the active player is White and 6 if it is Black
    def getPawnStartRank(self):
        if self.ToMove == whiteChar:
            return 1
        else:
            return 6

    #Does basic checks on if a piece is on the board where the move finder has been told
        #param rankIndex: rank the piece is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the piece is on. 0 = a-file, 1 = b-file, etc.
    def moveSanityChecks(self, rankIndex, fileIndex):
        if rankIndex < 0 or rankIndex > 7:
            print(rankIndex)
            raise Exception("Piece in the wrong place")
        if self.Board[rankIndex][fileIndex][0] != self.ToMove:
            raise Exception("Looking for the wrong color")

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
        #TODO: en passant
    def findPawnMoves(self, rankIndex, fileIndex):
        self.moveSanityChecks(rankIndex, fileIndex)
        moves = []
        direction, startRank = self.getPawnDirection(rankIndex, fileIndex)
        #TODO: check for check
        if self.Board[rankIndex + direction][fileIndex] == emptySquare:
            moves.append(fileITA[fileIndex] + rankITA[rankIndex + direction])
            if rankIndex == startRank and self.Board[rankIndex + direction + direction][fileIndex] == emptySquare:
                moves.append(fileITA[fileIndex] + rankITA[rankIndex + direction + direction])
        if fileIndex > 0:
            if self.Board[rankIndex + direction][fileIndex - 1][0] == opponent[self.ToMove]:
                moves.append(fileITA[fileIndex] + 'x' + fileITA[fileIndex - 1] + rankITA[rankIndex + direction])
        if fileIndex < 7:
            if self.Board[rankIndex + direction][fileIndex + 1][0] == opponent[self.ToMove]:
                moves.append(fileITA[fileIndex] + 'x' + fileITA[fileIndex + 1] + rankITA[rankIndex + direction])
        return moves

    #Finds moves a particular knight can make
        #param rankIndex: rank the knight is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the knight is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the knight can make. Nf3, Nbd2, Nxd4, etc.
    def findKnightMoves(self, rankIndex, fileIndex):
        self.moveSanityChecks(rankIndex, fileIndex)
        moves = []
        moveIndices = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
        #TODO: check for check
        #TODO: conflicts
        for moveIndex in moveIndices:
            targetRankIndex = rankIndex + moveIndex[0]
            targetFileIndex = fileIndex + moveIndex[1]
            if targetRankIndex > 7 or targetRankIndex < 0 or targetFileIndex > 7 or targetFileIndex < 0:
                continue
            if self.Board[targetRankIndex][targetFileIndex] == emptySquare:
                moves.append(knightChar + fileITA[targetFileIndex] + rankITA[targetRankIndex])
            elif self.Board[targetRankIndex][targetFileIndex][0] == opponent[self.ToMove]:
                moves.append(knightChar + 'x' + fileITA[targetFileIndex] + rankITA[targetRankIndex])
        return moves

    #Finds moves a particular bishop can make
        #param rankIndex: rank the bishop is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the bishop is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the bishop can make. Bb5, Bxf6, etc.
    def findBishopMoves(self, rankIndex, fileIndex, piece=bishopChar):
        self.moveSanityChecks(rankIndex, fileIndex)
        moves = []
        moveDirections = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        #TODO: check for check
        #TODO: conflicts
        for moveDirection in moveDirections:
            targetRankIndex = rankIndex
            targetFileIndex = fileIndex
            while True:
                targetRankIndex += moveDirection[0]
                targetFileIndex += moveDirection[1]
                if targetRankIndex > 7 or targetRankIndex < 0 or targetFileIndex > 7 or targetFileIndex < 0:
                    break
                if self.Board[targetRankIndex][targetFileIndex] == emptySquare:
                    moves.append(piece + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                elif self.Board[targetRankIndex][targetFileIndex][0] == opponent[self.ToMove]:
                    moves.append(piece + 'x' + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                    break
                elif self.Board[targetRankIndex][targetFileIndex][0] == self.ToMove:
                    break
                else: #something has gone wrong
                    raise Exception("unidentified piece present")
        return moves

    #Finds moves a particular rook can make
        #param rankIndex: rank the rook is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the rook is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the rook can make. Rd1, Rxe5, etc.
    def findRookMoves(self, rankIndex, fileIndex, piece=rookChar):
        self.moveSanityChecks(rankIndex, fileIndex)
        moves = []
        moveDirections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #TODO: check for check
        #TODO: conflicts
        for moveDirection in moveDirections:
            targetRankIndex = rankIndex
            targetFileIndex = fileIndex
            while True:
                targetRankIndex += moveDirection[0]
                targetFileIndex += moveDirection[1]
                if targetRankIndex > 7 or targetRankIndex < 0 or targetFileIndex > 7 or targetFileIndex < 0:
                    break
                if self.Board[targetRankIndex][targetFileIndex] == emptySquare:
                    moves.append(piece + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                elif self.Board[targetRankIndex][targetFileIndex][0] == opponent[self.ToMove]:
                    moves.append(piece + 'x' + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                    break
                elif self.Board[targetRankIndex][targetFileIndex][0] == self.ToMove:
                    break
                else: #something has gone wrong
                    raise Exception("unidentified piece present")
        return moves

    #Finds moves a particular rook can make
        #param rankIndex: rank the queen is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the queen is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the rook can make. Qe8, Qxe5, etc.
    def findQueenMoves(self, rankIndex, fileIndex):
        moves = self.findBishopMoves(rankIndex, fileIndex, queenChar)
        moves.extend(self.findRookMoves(rankIndex, fileIndex, queenChar))
        return moves

    #Finds moves a particular king can make
        #param rankIndex: rank the king is on. 0 = 1st rank, 1 = 2nd, etc.
        #param fileIndex: file the king is on. 0 = a-file, 1 = b-file, etc.
        #returns: list of moves that the king can make. Ke2, Kxc7, etc.
    def findKingMoves(self, rankIndex, fileIndex):
        self.moveSanityChecks(rankIndex, fileIndex)
        moves = []
        moveDirections = [-1, 0, 1]
        #TODO: check for check
        #TODO (all): can't take king
        #TODO: castling
        for rankDirection in list(moveDirections):
            for fileDirection in list(moveDirections):
                if not rankDirection and not fileDirection:
                    continue
                targetRankIndex = rankIndex + rankDirection
                targetFileIndex = fileIndex + fileDirection
                if targetRankIndex > 7 or targetRankIndex < 0 or targetFileIndex > 7 or targetFileIndex < 0:
                    continue
                if self.Board[targetRankIndex][targetFileIndex] == emptySquare:
                    moves.append(kingChar + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                elif self.Board[targetRankIndex][targetFileIndex][0] == opponent[self.ToMove]:
                    moves.append(kingChar + 'x' + fileITA[targetFileIndex] + rankITA[targetRankIndex])
                elif self.Board[targetRankIndex][targetFileIndex][0] == self.ToMove:
                    continue
                else: #something has gone wrong
                    raise Exception("unidentified piece present")
        return moves

    #Accepts a move and makes it on the chessboard
        #param move: a legal chess move that can be taken by the active player. e3, exd4, Nf3, O-O-O, etc.
    def MakeMove(self, move):
        #figure out which piece type is moving
        result = True
        if move[0] in fileITA.values():
            result = self.makePawnMove(move)
        elif move[0] == knightChar:
            result = self.makeKnightMove(move)
        elif move[0] == bishopChar:
            result = self.makeBishopMove(move)
        elif move[0] == rookChar:
            result = self.makeRookMove(move)
        elif move[0] == queenChar:
            result = self.makeQueenMove(move)
        elif move[0] == kingChar:
            result = self.makeKingMove(move)
        else:
            raise Exception('The heck piece are you trying to move')
        if not result:
            raise Exception('The heck move are you trying to make')
        #TODO: other pieces
        self.ToMove = opponent[self.ToMove]

    #Accepts a pawn move and makes it on the chessboard
        #param move: a legal pawn move that can be taken by the active player. e3, exd4, e8=Q, etc.
    def makePawnMove(self, move):
        direction = self.getColorDirection()
        if 'x' in move:
            targetFileIndex = fileATI[move[2]]
            sourceFileIndex = fileATI[move[0]]
            targetRankIndex = rankATI[move[3]]
            sourceRankIndex = rankATI[move[3]] - direction
        else:
            targetFileIndex = fileATI[move[0]]
            sourceFileIndex = fileATI[move[0]]
            targetRankIndex = rankATI[move[1]]
            if self.Board[targetRankIndex - direction][sourceFileIndex] == self.ToMove + pawnChar:
                sourceRankIndex = targetRankIndex - direction
            elif self.Board[targetRankIndex - direction][sourceFileIndex] == emptySquare:
                sourceRankIndex = targetRankIndex - direction - direction
                if sourceRankIndex != self.getPawnStartRank():
                    raise Exception("Can't move the pawn like that")
        #TODO: copy board, make move on copy, check it, and set it to be the real board
        #TODO: promotion
        if self.Board[sourceRankIndex][sourceFileIndex] != self.ToMove + pawnChar:
            print(self.Board[sourceRankIndex][sourceFileIndex])
            raise Exception("No pawn here")
        if self.Board[targetRankIndex][targetFileIndex] != emptySquare and 'x' not in move:
            raise Exception("Can't move here")
        self.Board[sourceRankIndex][sourceFileIndex] = emptySquare
        self.Board[targetRankIndex][targetFileIndex] = self.ToMove + pawnChar
        return True

    #Accepts a knight move and makes it on the chessboard
        #param move: a legal knight move that can be taken by the active player. Nf3, Nbd2, Nxd4, etc.
    def makeKnightMove(self, move):
        targetFileIndex = fileATI[move[-2]]
        targetRankIndex = rankATI[move[-1]]
        moveIndices = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
        for moveIndex in moveIndices:
            #TODO: conflicts
            sourceRankIndex = targetRankIndex + moveIndex[0]
            sourceFileIndex = targetFileIndex + moveIndex[1]
            if sourceRankIndex > 7 or sourceRankIndex < 0 or sourceFileIndex > 7 or sourceFileIndex < 0:
                continue
            if self.Board[sourceRankIndex][sourceFileIndex] == self.ToMove + knightChar:
                break
        if self.Board[sourceRankIndex][sourceFileIndex] != self.ToMove + knightChar:
            raise Exception("No knight here")
        if self.Board[targetRankIndex][targetFileIndex] != emptySquare and 'x' not in move:
            raise Exception("Can't move here")
        self.Board[sourceRankIndex][sourceFileIndex] = emptySquare
        self.Board[targetRankIndex][targetFileIndex] = self.ToMove + knightChar
        return True

    #Accepts a bishop move and makes it on the chessboard
        #param move: a legal bishop move that can be taken by the active player. Bb5, Bxf6, etc.
    def makeBishopMove(self, move, piece=bishopChar):
        targetFileIndex = fileATI[move[-2]]
        targetRankIndex = rankATI[move[-1]]
        moveDirections = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        #TODO: conflicts
        for moveDirection in moveDirections:
            sourceRankIndex = targetRankIndex
            sourceFileIndex = targetFileIndex
            while True:
                sourceRankIndex += moveDirection[0]
                sourceFileIndex += moveDirection[1]
                if sourceRankIndex > 7 or sourceRankIndex < 0 or sourceFileIndex > 7 or sourceFileIndex < 0:
                    break
                if self.Board[sourceRankIndex][sourceFileIndex] == self.ToMove + piece:
                    self.Board[sourceRankIndex][sourceFileIndex] = emptySquare
                    self.Board[targetRankIndex][targetFileIndex] = self.ToMove + piece
                    return True
                if self.Board[sourceRankIndex][sourceFileIndex] == emptySquare:
                    continue
                break

    #Accepts a rook move and makes it on the chessboard
        #param move: a legal rook move that can be taken by the active player. Rd1, Rxe5, etc.
    def makeRookMove(self, move, piece=rookChar):
        targetFileIndex = fileATI[move[-2]]
        targetRankIndex = rankATI[move[-1]]
        moveDirections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #TODO: conflicts
        for moveDirection in moveDirections:
            sourceRankIndex = targetRankIndex
            sourceFileIndex = targetFileIndex
            while True:
                sourceRankIndex += moveDirection[0]
                sourceFileIndex += moveDirection[1]
                if sourceRankIndex > 7 or sourceRankIndex < 0 or sourceFileIndex > 7 or sourceFileIndex < 0:
                    break
                if self.Board[sourceRankIndex][sourceFileIndex] == self.ToMove + piece:
                    self.Board[sourceRankIndex][sourceFileIndex] = emptySquare
                    self.Board[targetRankIndex][targetFileIndex] = self.ToMove + piece
                    return True
                if self.Board[sourceRankIndex][sourceFileIndex] == emptySquare:
                    continue
                break

    #Accepts a queen move and makes it on the chessboard
        #param move: a legal queen move that can be taken by the active player. Qe8, Qxe5, etc.
    def makeQueenMove(self, move):
        if not self.makeBishopMove(move, queenChar):
            return self.makeRookMove(move, queenChar)
        return True

    #Accepts a king move and makes it on the chessboard
        #param move: a legal king move that can be taken by the active player. Ke2, Kxc7, etc.
    def makeKingMove(self, move):
        targetFileIndex = fileATI[move[-2]]
        targetRankIndex = rankATI[move[-1]]
        moveDirections = [-1, 0, 1]
        for fileDirection in list(moveDirections):
            for rankDirection in list(moveDirections):
                sourceRankIndex = targetRankIndex + rankDirection
                sourceFileIndex = targetFileIndex + fileDirection
                if sourceRankIndex > 7 or sourceRankIndex < 0 or sourceFileIndex > 7 or sourceFileIndex < 0:
                    break
                if self.Board[sourceRankIndex][sourceFileIndex] == self.ToMove + kingChar:
                    self.Board[sourceRankIndex][sourceFileIndex] = emptySquare
                    self.Board[targetRankIndex][targetFileIndex] = self.ToMove + kingChar
                    return True






