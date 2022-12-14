
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
        self.gameMode = "Simple"
        

    
    # get random token either S or O
    def getRandomToken(self):
        import random
        tokens = ["S", "O"]
        return random.choice(tokens)

    # Get list of all empty spaces
    def getEmptySpaces(self):
        emptySpaces = []
        for row in range(self.boardSize):
            for column in range(self.boardSize):
                if self.board[row][column] == "":
                    emptySpaces.append([row, column])
        return emptySpaces

    # Def choose random empty space
    def chooseRandomEmptySpace(self):
        import random
        emptySpaces = self.getEmptySpaces()
        return random.choice(emptySpaces)

    def printPoints(self):
        print("Player 1: " + str(self.player1Points))
        print("Player 2: " + str(self.player2Points))
        print('=====================')

    def getPlayerPoints(self, player):
        if player == 1:
            return self.player1Points
        else:
            return self.player2Points

    def updateGameMode(self, newMode):
        if newMode == "Simple" or newMode == "General":
            self.gameMode = newMode
        return self.gameMode    

    def getWindowSize(self, boardSize):
        #Dictionary for boardSizes 3 - 10 that hold a list of width and height for the window
        windowSizeDict = {3: [280, 500], 4: [280, 500], 5: [320, 550], 6: [330, 570], 7: [385, 576], 8: [440, 600], 9: [495, 610], 10: [550, 670]}
        width = windowSizeDict[boardSize][0]
        height = windowSizeDict[boardSize][1]
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
        elif self.board[row][column] != "":
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
        self.player1Points = 0
        self.player2Points = 0
        self.createBoard()

    def updateBoardSize(self, newSize):
        errorMessage = ""
        
        # if input is not a number, return error message
        if not newSize.isdigit():
            errorMessage = "Please enter a valid number"
            return self.boardSize, errorMessage


        if int(newSize) > 10:
            errorMessage = "Board size cannot be greater than 10"
            newSize = 10
        if int(newSize) < 3:
            errorMessage = "Board size cannot be less than 3"
            newSize = 3
        self.boardSize = newSize
        self.resetBoard(int(self.boardSize))
        return self.boardSize, errorMessage


    def addPoint(self, player):
        if player == 1:
            self.player1Points += 1
        else:
            self.player2Points += 1


    def checkSPlacedPoint(self, row, column, player):
        '''
        [ This is the point->S / /
        / O /
        / / S]
        '''

        try:
            if self.board[row+1][column+1][0] == "O":
                if self.board[row+2][column+2][0] == "S":
                    self.addPoint(player)
                    print("->S / / \n/ O /\n/ / S")
        except:
            pass

        '''
        [->S / /
        O / /
        S / / ]
        '''
        
        try:
            if self.board[row+1][column][0] == "O":
                if self.board[row+2][column][0] == "S":
                    self.addPoint(player)
                    print("->S\nO\nS")
        except:
            pass

        '''
        [ / / ->S]
        [ / O /]
        [ S / /]
        '''
        
        try:
            if self.board[row+1][column-1][0] == "O":
                if self.board[row+2][column-2][0] == "S":
                    self.addPoint(player)
                    print("/ / ->S\n/ O /\nS / /")
        except:
            pass

        '''
        [S O S <-]
        '''
        
        try:
            if self.board[row][column-1][0] == "O":
                if self.board[row][column-2][0] == "S":
                    self.addPoint(player)
                    print("S O S <-")
        except:
            pass


        '''
        [S / /
        / O /
        / / S <- This is the point]
        '''
        
        try: 
            if self.board[row-1][column-1][0] == "O":
                if self.board[row-2][column-2][0] == "S":
                    self.addPoint(player)
                    print("S / /\n/ O /\n/ / S<-")
        except:
            pass

        '''
        [S / /
        O / /
        -> S / / ]
        '''
        
        try:
            if self.board[row-1][column][0] == "O":
                if self.board[row-2][column][0] == "S":
                    self.addPoint(player)
                    print("S\nO\nS<-")
        except:
            pass

        '''
        [ / / S]
        [ / O /]
        [ -> S / /]
        '''
        
        try:
            if self.board[row-1][column+1][0] == "O":
                if self.board[row-2][column+2][0] == "S":
                    self.addPoint(player)
                    print("S / /\n O / /\n -> S / /")
        except:
            pass

        '''
        [-> S O S]
        '''
        
        try:
            if self.board[row][column+1][0] == "O":
                if self.board[row][column+2][0] == "S":
                    self.addPoint(player)
                    print("-> S O S")
        except:
            pass
    
    def checkOPlacedPoint(self,row,column,player):

        '''
        [S
        ->O
        S]
        '''
        
        try:
            if self.board[row-1][column][0] == "S":
                if self.board[row+1][column][0] == "S":
                    self.addPoint(player)
                    print("S\n->O\nS")
        except:
            pass

        '''
        [S O<- S]
        '''
        
        try:
            if self.board[row][column-1][0] == "S":
                if self.board[row][column+1][0] == "S":
                    self.addPoint(player)
                    print(" [S O<- S]")
        except:
            pass

        '''
        [S / /
        / O<- /
        / / S]
        '''
        
        try:
            if self.board[row-1][column-1][0] == "S":
                if self.board[row+1][column+1][0] == "S":
                    self.addPoint(player)
                    print("[S / / \n/ O<- /\n/ / S]")
        except:
            pass

        '''
        [/ / S
        / O<- /
        S / /]
        '''
        
        try:
            if self.board[row-1][column+1][0] == "S":
                if self.board[row+1][column-1][0] == "S":
                    self.addPoint(player)
                    print("[/ / S \n/ O<- /\nS / /]")
        except:
            pass


    def checkForSimpleWin(self):
        if self.player1Points >= 1 or self.player2Points >= 1:
            return True
        else:
            return False

    def getGeneralWinner(self):
        if self.player1Points > self.player2Points:
            return 1
        elif self.player2Points > self.player1Points:
            return 2
        else:
            return 0