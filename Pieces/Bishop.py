from Pieces.Piece import Piece

class Bishop(Piece):

    def possibleMoves(self):
        moves = []
        x = self.x + 1
        y = self.y + 1 
        while self.board.isOn(x,y):
            if self.isFree(x,y):
                moves.append((x, y))
            if self.board.get(x,y) is not None:
                break
            x += 1
            y += 1
        x = self.x - 1
        y = self.y - 1
        while self.board.isOn(x,y):
            if self.isFree(x,y):
                moves.append((x, y))
            if self.board.get(x,y) is not None:
                break
            x -= 1
            y -= 1
        x = self.x - 1
        y = self.y + 1
        while self.board.isOn(x,y):
            if self.isFree(x,y):
                moves.append((x, y))
            if self.board.get(x,y) is not None:
                break
            x -= 1
            y += 1
        x = self.x + 1
        y = self.y - 1
        while self.board.isOn(x,y):
            if self.isFree(x,y):
                moves.append((x, y))
            if self.board.get(x,y) is not None:
                break
            x += 1
            y -= 1
        self.checkMoves(moves)
        return moves

    
