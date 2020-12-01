from Pieces.Piece import Piece

class Knight(Piece):

    def possibleMoves(self):
        moves = []
        for x,y in [
        (self.x+2, self.y+1),
        (self.x+2, self.y-1),
        (self.x-2, self.y+1),
        (self.x-2, self.y-1),
        (self.x+1, self.y+2),
        (self.x-1, self.y+2),
        (self.x+1, self.y-2),
        (self.x-1, self.y-2)]:
            if self.board.isOn(x,y):
                if self.isFree(x,y):
                    moves.append((x, y))
        self.checkMoves(moves)
        return moves

    
