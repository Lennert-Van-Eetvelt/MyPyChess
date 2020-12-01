import copy
from Board import Board
class Piece(object):
    def __init__(self, board, y, x, color):
        self.color = color
        self.x = x
        self.y = y
        board.place(self, x, y)
        self.board = board
       
        self.name = self.__class__.__name__

        self.alive = True
        self.moves = [(x,y)]

    def move(self, x, y):
        self.board.moves.append((self,x,y, self.x, self.y))
        self.moves.append((x,y))

        x_old = self.x
        y_old = self.y
        self.x = x
        self.y = y

        self.board.clean(x_old,y_old)
        self.board.place(self, x, y)

    def possibleMoves(self):
        return []

    def moved(self):
        return len(self.moves) is not 1

    def kill(self):
        self.alive = False
        if self.name is "King":
            print(self.color + " lost the game")

    def isFree(self, x, y):
        return self.board.get(x, y) is None or (self.board.get(x,y) is not self and self.board.get(x,y).color is not self.color)
    

    def isLegalMove(self, x, y):
        newboard = copy.deepcopy(self.board)
        newboard.isReal = False
        newboard.get(self.x,self.y).board.isReal = False
        newboard.get(self.x,self.y).move(x,y)
        color = "White" if self.color is 'White' else 'Black'
        return not newboard.isCheck(color)

    def checkMoves(self, moves):
        if self.board.isReal:
            i = 0
            while i <len(moves):
                if i< len(moves) and not self.isLegalMove(*moves[i]):
                        moves.pop(i)
                        i += -1
                i +=1

    def __repr__(self):
        if self.alive is False:
            return "(dead " + self.name + "  " +  self.color + ")"
        return "("+self.name + "  " +  self.color+")"
