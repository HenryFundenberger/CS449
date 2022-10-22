from cgitb import text
from select import select
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT, ttk
from tkinter import messagebox

#Create GUI class that inherits a game logic class
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SOS Game - Henry Fundenberger")
        self.geometry("450x600")
        self.resizable(True, True)
        self.Player = 1
        self.board_size = 8
        self.player1Points = 0
        self.player2Points = 0
        self.testVar = False
        self.gameMode = "simple"
        self.minY = 400
        self.CurrentPlayerLabel = tk.Label(self, text="Playing: Player 1")
        # Update Icon for Window
        self.iconbitmap("SOS.ico")

        self.create_widgets()

    def create_widgets(self):
        # Create frame for Board Title and widgets
        self.board_frame = tk.Frame(self)
        self.board_frame.pack(pady=10)

        #Create label in center of window inside board_frame
        self.label = tk.Label(self.board_frame, text="SOS Game", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, padx=0, pady=0)

        # Create Label for Board Size
        self.board_size_label = tk.Label(self.board_frame, text="Board Size: ")
        self.board_size_label.grid(row=1, column=0, padx=0, pady=0)

        # Create entry box to update board size and after pressing enter, update board size
        self.board_size_entry = tk.Entry(self.board_frame, width=3)
        self.board_size_entry.grid(row=1, column=1, padx=0, pady=0)
        self.board_size_entry.bind("<Return>", self.update_board_size)

        self.CurrentPlayerLabel.pack(pady=10)

        # Create frame for game mode selection and widgets
        self.game_mode_frame = tk.Frame(self)
        #Include 2 radio buttons one labeled simple and one labeled general
        #And reset the board when the radio button is clicked
        self.game_mode_var = tk.StringVar()
        self.game_mode_var.set("simple")
        self.game_mode_frame.pack(pady=10)
        self.game_mode_label = tk.Label(self.game_mode_frame, text="Game Mode: ")
        self.game_mode_simple = tk.Radiobutton(self.game_mode_frame, text="Simple", variable=self.game_mode_var, value="simple", command=self.reset)
        self.game_mode_simple.grid(row=0, column=0,