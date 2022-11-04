from select import select
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT, ttk
from tkinter import messagebox
from turtle import update
from GUI import App
from board import Board

# Test class that inherits from the Board class
class UnitTestClass:
    def __init__(self,size):
        self.board = Board(size)
        
def test_ChooseBoardSize():
    test = UnitTestClass(3)
    updateValue = 10
    value = test.board.updateBoardSize(str(updateValue))[0]
    test.board.placePiece(value-1, value-1, "X", 1)
    assert test.board.getPiece(9, 9)[0] == "X" and test.board.boardSize == 10


def test_ChooseInvalidBoardSize():
    test = UnitTestClass(3)
    updateValue = 15
    value = test.board.updateBoardSize(str(updateValue))[0]
    test.board.placePiece(value-1, value-1, "X", 1)
    assert test.board.getPiece(9, 9)[0] == "X" and test.board.boardSize == 10

def test_ChooseValidGameMode():
    test = UnitTestClass(3)
    oldGameMode = test.board.gameMode
    test.board.updateGameMode("General")
    assert oldGameMode == "Simple" and test.board.gameMode == "General"

def test_ChooseInvalidGameMode():
    test = UnitTestClass(3)
    oldGameMode = test.board.gameMode
    test.board.updateGameMode("Invalid")
    assert oldGameMode == "Simple" and test.board.gameMode == "Simple"

def test_MakeSimpleGameMove():
    test = UnitTestClass(3)
    test.board.placePiece(0, 0, "S", 1)
    assert test.board.getPiece(0, 0)[0] == "S" and test.board.gameMode == "Simple" and test.board.getPiece(0, 0)[1] == 1

def test_MakeInvalidSimpleGameMove():
    test = UnitTestClass(3)
    test.board.placePiece(0, 0, "S", 1)
    test.board.placePiece(0, 0, "O", 2)
    assert test.board.getPiece(0, 0)[0] == "S" and test.board.gameMode == "Simple" and test.board.getPiece(0, 0)[1] == 1

def test_MakeGeneralGameMove():
    test = UnitTestClass(3)
    test.board.updateGameMode("General")
    test.board.placePiece(0, 0, "S", 1)
    assert test.board.getPiece(0, 0)[0] == "S" and test.board.gameMode == "General" and test.board.getPiece(0, 0)[1] == 1

def test_MakeInvalidGeneralGameMove():
    test = UnitTestClass(3)
    test.board.updateGameMode("General")
    test.board.placePiece(0, 0, "S", 1)
    test.board.placePiece(0, 0, "O", 2)
    assert test.board.getPiece(0, 0)[0] == "S" and test.board.gameMode == "General" and test.board.getPiece(0, 0)[1] == 1

def test_StartGeneralGame():
    testApp = App()
    testApp.board_size_slider.set(5)
    testApp.game_mode_var.set("General")
    testApp.after(100, lambda: testApp.start_button.invoke())
    testApp.after(200, lambda: testApp.destroy())
    testApp.mainloop()
    assert testApp.gameStarted == True and testApp.board.board != [] and testApp.board.boardSize == 5 and testApp.board.gameMode == "General"

def test_StartSimpleGame():
    testApp = App()
    testApp.board_size_slider.set(11)
    testApp.game_mode_var.set("Simple")
    testApp.after(100, lambda: testApp.start_button.invoke())
    testApp.after(200, lambda: testApp.destroy())
    testApp.mainloop()
    assert testApp.gameStarted == True and testApp.board.board != [] and testApp.board.boardSize == 10 and testApp.board.gameMode == "Simple"

def test_SimpleGameIsOverWin():
    test = UnitTestClass(3)
    test.board.placePiece(0, 0, "S", 1)
    test.board.checkSPlacedPoint(0,0,1)
    test.board.placePiece(0, 1, "O", 2)
    test.board.checkOPlacedPoint(0,1,1)
    test.board.placePiece(0, 2, "S", 1)
    test.board.checkSPlacedPoint(0,2,1)
    if(test.board.checkForSimpleWin()):
        assert test.board.getGeneralWinner() == 1

def test_SimpleGameIsOverTie():
    test = UnitTestClass(3)
    test.board.placePiece(0, 0, "S", 1)
    test.board.checkSPlacedPoint(0,0,1)
    test.board.placePiece(0, 1, "S", 2)
    test.board.checkSPlacedPoint(0,1,2)
    test.board.placePiece(0, 2, "S", 1)
    test.board.checkSPlacedPoint(0,2,1)
    test.board.placePiece(1, 0, "S", 2)
    test.board.checkSPlacedPoint(1,0,2)
    test.board.placePiece(1, 1, "S", 1)
    test.board.checkSPlacedPoint(1,1,1)
    test.board.placePiece(1, 2, "S", 2)
    test.board.checkSPlacedPoint(1,2,2)
    test.board.placePiece(2, 0, "S", 1)
    test.board.checkSPlacedPoint(2,0,1)
    test.board.placePiece(2, 1, "S", 2)
    test.board.checkSPlacedPoint(2,1,2)
    test.board.placePiece(2, 2, "S", 1)
    test.board.checkSPlacedPoint(2,2,1)
    if(test.board.checkForSimpleWin() == False):
        assert test.board.getGeneralWinner() == 0

def test_GeneralGameIsOverWin():
    test = UnitTestClass(3)
    test.board.updateGameMode("General")
    test.board.placePiece(0, 0, "S", 1)
    test.board.checkSPlacedPoint(0,0,1)
    test.board.placePiece(0, 1, "O", 2)
    test.board.checkOPlacedPoint(0,1,2)
    test.board.placePiece(0, 2, "S", 1)
    test.board.checkSPlacedPoint(0,2,1)
    test.board.placePiece(1, 0, "S", 2)
    test.board.checkSPlacedPoint(1,0,2)
    test.board.placePiece(1, 1, "S", 1)
    test.board.checkSPlacedPoint(1,1,1)
    test.board.placePiece(1, 2, "S", 2)
    test.board.checkSPlacedPoint(1,2,2)
    test.board.placePiece(2, 0, "S", 1)
    test.board.checkSPlacedPoint(2,0,1)
    test.board.placePiece(2, 1, "S", 2)
    test.board.checkSPlacedPoint(2,1,2)
    test.board.placePiece(2, 2, "S", 1)
    test.board.checkSPlacedPoint(2,2,1)
    if(test.board.noOpenSpaces()):
        assert test.board.getGeneralWinner() == 1

def test_GeneralGameIsOverTie():
    test = UnitTestClass(3)
    test.board.updateGameMode("General")
    test.board.placePiece(0, 0, "S", 1)
    test.board.checkSPlacedPoint(0,0,1)
    test.board.placePiece(0, 1, "S", 2)
    test.board.checkSPlacedPoint(0,1,2)
    test.board.placePiece(0, 2, "S", 1)
    test.board.checkSPlacedPoint(0,2,1)
    test.board.placePiece(1, 0, "S", 2)
    test.board.checkSPlacedPoint(1,0,2)
    test.board.placePiece(1, 1, "S", 1)
    test.board.checkSPlacedPoint(1,1,1)
    test.board.placePiece(1, 2, "S", 2)
    test.board.checkSPlacedPoint(1,2,2)
    test.board.placePiece(2, 0, "S", 1)
    test.board.checkSPlacedPoint(2,0,1)
    test.board.placePiece(2, 1, "S", 2)
    test.board.checkSPlacedPoint(2,1,2)
    test.board.placePiece(2, 2, "S", 1)
    test.board.checkSPlacedPoint(2,2,1)
    if(test.board.noOpenSpaces()):
        assert test.board.getGeneralWinner() == 0
