from cgitb import text
from select import select
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT, ttk
from tkinter import messagebox
from main import App
import pytest

#extends the App class to test the functions
class NewTestApp(App):
    # Create App
    def __init__(self):
        super().__init__()
        self.buttonTest = ""
        self.testVar = ""
        self.player1Var = ""
        self.player2Var = ""

    def test_ResizeBoard(self):
        #Test resize board
        self.board_size_entry.delete(0, tk.END)
        self.board_size_entry.insert(0, "3")
        self.board_size = 3
        #Delete all buttons
        for widget in self.frame.winfo_children():
            widget.destroy()
        #Create new buttons
        for row in range(self.board_size):
            for column in range(self.board_size):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=2)
                # Add blue background to buttons
                button = ttk.Button(self.frame, text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)
        # Update Window Size
        self.geometry(str(self.board_size * 55) + "x" + str(self.minY))
        # Keep Y size constant
        self.minsize(str(self.board_size * 55), self.minY)
        #Reset Player to 1
        self.Player = 1
        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=10, padx=0, pady=0)

        # Test button in 3x3 board bottom right
        button = self.frame.winfo_children()[8]
        button.configure(text="S")
        self.buttonTest = button["text"]

    def test_InvalidBoardSize(self):
        self.board_size_entry.delete(0, tk.END)
        self.board_size_entry.insert(0, "0")
        self.board_size = 0
        if self.board_size < 3:
            self.board_size = 3
            self.board_size_entry.delete(0, tk.END)
            self.board_size_entry.insert(0, "3")
        if self.board_size > 10:
            self.board_size = 10
            self.board_size_entry.delete(0, tk.END)
            self.board_size_entry.insert(0, "10")
        self.testVar = self.board_size
        #Delete all buttons
        for widget in self.frame.winfo_children():
            widget.destroy()
        #Create new buttons
        for row in range(self.board_size):
            for column in range(self.board_size):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=2)
                # Add blue background to buttons
                button = ttk.Button(self.frame, text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)
        # Update Window Size
        self.geometry(str(self.board_size * 55) + "x" + str(self.minY))
        # Keep Y size constant
        self.minsize(str(self.board_size * 55), self.minY)
        #Reset Player to 1
        self.Player = 1
        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=10, padx=0, pady=0)
        #place move at third col third row
        button = self.frame.winfo_children()[8]
        button.configure(text="S")
        self.buttonTest = button["text"]



    def test_chooseGameMode(self):
        self.game_mode_var.set("general")
        self.testVar = self.game_mode_var.get()

    def test_MakeMove(self):
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        self.buttonTest = button["text"]
        self.updateCurrentPlayerText()

    def test_MakeMoveGeneralGameMode(self):
        self.game_mode_var.set("general")
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        self.buttonTest = button["text"]
        self.updateCurrentPlayerText()
        self.buttonTest = self.Player
        self.testVar = self.game_mode_var.get()

    def test_MakeInvalidMoveGeneralGameMode(self):
        self.game_mode_var.set("general")
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        if button["text"] == " ":
            button.configure(text="O")
        self.buttonTest = button["text"]
        self.testVar = self.game_mode_var.get()

    def test_MakeMoveSimpleGameMode(self):
        self.game_mode_var.set("simple")
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        self.buttonTest = button["text"]
        self.updateCurrentPlayerText()
        self.buttonTest = self.Player
        self.testVar = self.game_mode_var.get()

    def test_MakeInvalidMoveSimpleGameMode(self):
        self.game_mode_var.set("simple")
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        self.buttonTest = button["text"]
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        if button["text"] == " ":
            button.configure(text="O")
        self.buttonTest = button["text"]
        self.testVar = self.game_mode_var.get()


    def test_StartNewGame(self):
        self.game_mode_var.set("simple")
        self.player1_var.set("S")
        self.player2_var.set("O")
        self.Player = 1
        self.updateCurrentPlayerText()
        #Get button at position 0
        button = self.frame.winfo_children()[0]
        button.configure(text="S")
        # Update Player
        self.Player = 2
        self.buttonTest = button["text"]
        self.updateCurrentPlayerText()
        self.buttonTest = self.Player
        self.testVar = self.game_mode_var.get()
        self.player1var = self.player1_var.get()
        self.player2var = self.player2_var.get()



#Main SECTION TEST FUNCTIONS
#---------------------------------------------------------------

def test_MakeMoveSimpleGameMove():
    app = NewTestApp()
    app.after(1000, app.test_MakeMoveSimpleGameMode())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.Player == 2 and app.testVar == "simple" 

def test_MakeInvalidSimpleGameMove():
    app = NewTestApp()
    app.after(1000, app.test_MakeInvalidMoveSimpleGameMode())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.buttonTest == "S" and app.testVar == "simple"

def test_MakeMoveGeneralGameMove():
    app = NewTestApp()
    app.after(1000, app.test_MakeMoveGeneralGameMode())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.Player == 2 and app.testVar == "general"


def test_MakeInvalidGeneralGameMove():
    app = NewTestApp()
    app.after(1000, app.test_MakeInvalidMoveGeneralGameMode())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.buttonTest == "S" and app.testVar == "general"   

def test_MakeMove():
    app = NewTestApp()
    app.after(1000, app.test_MakeMove())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.Player == 2

def test_chooseGameMode():
    app = NewTestApp()
    app.after(1000, app.test_chooseGameMode())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.testVar == "general"

def test_ResizeBoard():
    app = NewTestApp()
    app.after(1000, app.test_ResizeBoard())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.board_size == 3 and app.buttonTest == "S"

def test_InvalidResizeBoard():
    app = NewTestApp()
    app.after(1000, app.test_InvalidBoardSize())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.testVar == 3 and app.buttonTest == "S"

def test_StartNewGame():
    app = NewTestApp()
    app.after(1000, app.test_StartNewGame())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.Player == 2 and app.testVar == "simple" and app.player1var == "S" and app.player2var == "O"

