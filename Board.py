import copy 

class Board(object):
    def __init__(self, size=8):
        board = []
        for y in range(size):
            board.append([])
            for x in range(size):
                board[y].append(None)
        self.board = board
        self.dead = []
        self.moves = []
        self.size = size
        self.state = 0
        self.states = {"" : 0 , "promotion" : 1, "check": 2, "checkmate": 3}
        self.isReal = True

    def place(self,piece, x, y):
        self.clean(x,y)
        self.board[y][x] = piece

    def clean(self, x, y):
        piece = self.board[y][x]
        if piece is not None and piece.x == x and piece.y == y: 
            piece.kill()
            self.dead.append(piece)
        self.board[y][x] = None

    def isOn(self, x, y):
        return x >= 0 and y >= 0 and x < self.size and y < self.size

    def get(self, x, y):
        if not self.isOn(x,y):
            return None
        return self.board[y][x]

    def cleanState(self):
        self.state = 0

    def setState(self, state):
        if self.states.get(state) > self.state:
            self.state = state

    def getState(self):
        return self.state
    
    def isCheck(self, color):
        for y in range(self.size):
            for x in range(self.size):
                piece = self.get(x,y)
                if piece is not None and piece.color is not color:
                    for move in piece.possibleMoves():
                        if self.get(*move) is not None and self.get(*move).name is "King" and piece.color is not self.get(*move):
                            return True
        return False
    def isCheckmate(self, color):
        for y in range(self.size):
            for x in range(self.size):
                piece = self.get(x,y)
                if piece is not None and piece.color is color:
                    if len(piece.possibleMoves()) >0:
                        return False
        if not self.isCheck(color):
            print('Stalemate')
            return False
        print("checkmate " + color +" has lost")
        return True

