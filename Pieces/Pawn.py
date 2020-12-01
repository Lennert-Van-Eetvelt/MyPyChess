from Pieces.Piece import Piece
from Pieces.Queen import Queen
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook
from Pieces.Knight import Knight

class Pawn(Piece):

    def possibleMoves(self):
        moves = []
        m = 1
        if self.color is "White":
            m = -1
        x = self.x
        y = self.y + m
        if self.board.isOn(x,y):
            if self.board.get(x, y) is None:
                moves.append((x, y))
                if not self.moved():
                    y += m
                    if self.board.isOn(x,y):
                        if self.board.get(x, y) is None:
                            moves.append((x, y))
        y = self.y + m
        for x in (self.x-1,self.x+1):
            if self.board.get(x,y) is not None and self.board.get(x,y).color is not self.color:
                moves.append((x,y))
        y = self.y
        for x in (self.x-1,self.x+1):
            if len(self.board.moves)>0:
                piece, moveX, moveY, oldX, oldY = self.board.moves[len(self.board.moves)-1]
                if self.board.get(x,y) is not None and  self.board.get(x,y).name is "Pawn" and  self.board.get(x,y).color is not self.color and x is moveX and y is moveY and len(piece.moves) is 2 and abs(moveY-oldY) is 2:
                    moves.append((x,y+m))
        self.checkMoves(moves)
        return moves

    def promote(self, newpiece):
        x = self.x
        y = self.y
        if "Queen" is newpiece.name:
            self.x = -1
            Queen(self.board, y, x, self.color)
            return True
        if "Rook" is newpiece.name:
            self.x = -1
            Rook(self.board,y,x, self.color)
            return True
        if "Bishop" is newpiece.name:
            self.x = -1
            Bishop(self.board, y, x, self.color)
            return True
        if "Knight" is newpiece.name:
            self.x = -1
            Knight(self.board, y, x, self.color)
            return True
        return False
        

    def move(self, x, y):
        Piece.move(self, x,y)
        m = 1        
        if self.color is "White":
            m = -1
        if len(self.board.moves)>1:
            piece, moveX, moveY, oldX, oldY = self.board.moves[len(self.board.moves)-2]
            if self.board.get(x,y-m) is not None and  self.board.get(x,y-m).name is "Pawn" and  self.board.get(x,y-m).color is not self.color and x is moveX and y-m is moveY and len(piece.moves) is 2 and  abs(moveY-oldY) is 2:
                self.board.clean(x,y-m)
        if self.color is "Black" and y is self.board.size-1:
            self.board.setState("promotion")
        if self.color is "White" and y is 0:
            self.board.setState("promotion")
