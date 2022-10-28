
# Create a board class that takes in a size

from distutils.log import error


class Board:

    def __init__(self, size):

        self.boardSize = size
        self.board = []
        self.createBoard()
        self.openSpaces = self.boardSize * self.boardSize
        self.player1Points = 0
        self.player2Points = 0

    def getWindowSize(self, boardSize):
        #Dictionary for boardSizes 3 - 10 that hold a list of width and height for the window
        myDict = {3: [280, 450], 4: [280, 450], 5: [320, 500], 6: [330, 520], 7: [385, 526], 8: [440, 550], 9: [495, 560], 10: [550, 620]}
        width = myDict[boardSize][0]
        height = myDict[boardSize][1]
        return [width, height]

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
            self.openSpaces -= 1
            return True

    def getPiece(self, row, column):
        return(self.board[row][column])


    #Print board
    def printBoard(self):
        for row in range(self.boardSize):
            print(self.board[row])

    def noOpenSpaces(self):
        if self.openSpaces == 0:
            return True
        else:
            return False

    def resetBoard(self, newSize):
        self.board = []
        self.boardSize = newSize
        self.openSpaces = self.boardSize * self.boardSize
        self.createBoard()

    def updateBoardSize(self, newSize):
        errorMessage = ""
        if int(newSize) > 10:
            errorMessage = "Board size cannot be greater than 10"
            newSize = 10
        if int(newSize) < 3:
            errorMessage = "Board size cannot be less than 3"
            newSize = 3
        self.boardSize = newSize
        self.resetBoard(int(self.boardSize))
        return self.boardSize, errorMessage


        
