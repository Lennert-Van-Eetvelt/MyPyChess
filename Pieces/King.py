from Pieces.Piece import Piece

class King(Piece):

    def possibleMoves(self):
        moves = []
        for x,y in [
        (self.x+1, self.y),
        (self.x-1, self.y),
        (self.x+1, self.y+1),
        (self.x-1, self.y-1),
        (self.x+1, self.y-1),
        (self.x-1, self.y+1),
        (self.x, self.y+1),
        (self.x, self.y-1)]:
            if self.board.isOn(x,y):
                if self.isFree(x,y):
                    moves.append((x, y))
        self.checkMoves(moves)
        return moves

    
