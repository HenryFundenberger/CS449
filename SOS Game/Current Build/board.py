
# Create a board class that takes in a size

class Board:

    def __init__(self, size):

        self.boardSize = size
        self.board = []
        self.createBoard()

    #Create board from lists of lists
    def createBoard(self):
        
        for row in range(self.boardSize):
            self.board.append([])
            for column in range(self.boardSize):
                self.board[row].append("")


    def placePiece(self, row, column, piece, player):
        # If space is out of bounds, return false
        if row < 0 or row >= self.boardSize or column < 0 or column >= self.boardSize:
            return False
        else:
            self.board[row][column] = [piece, player]
            return True

    def getPiece(self, row, column):
        return(self.board[row][column])


    #Print board
    def printBoard(self):
        for row in range(self.boardSize):
            print(self.board[row])


    def resetBoard(self, newSize):
        self.board = []
        self.boardSize = newSize
        self.createBoard()
