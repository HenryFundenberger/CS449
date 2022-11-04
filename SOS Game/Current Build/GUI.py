# Henry Fundenberger
# Student ID: 16251041
# CS 449

'''
This is the GUI file for the SOS game. It contains the GUI class, which builds the visual interface for the game.
It refernces the board class for the game logic but also has some of its own logic for the GUI.
'''


from select import select
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT, ttk
from tkinter import messagebox
from board import Board

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Sets the style of the GUI
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'white', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active','black')], forground=[('active','white')])
        self.title("SOS Game - Henry Fundenberger")

        self.gameStarted = False
        self.Player = 1
        self.board_size = 5
        self.CurrentPlayerLabel = tk.Label(self, text="Playing: Player 1")
        self.iconbitmap( 'SOS.ico')
        # Our board object refernce to control the game logic
        self.board = Board(self.board_size)
        self.boardWidth, self.boardHeight = self.board.getWindowSize(self.board_size)
        # Geometry for start window 
        self.geometry(str(self.boardWidth) + "x250" )
        # List to keep track of frames so they can be destroyed when switching between menus
        self.frameList = []
        # First build the start menu
        self.buildStartMenu()



    # Build start menu for game where you can choose game mode and board size then pass those values to the buildMainGame function
    def buildStartMenu(self):
        # Start Menu Frame
        self.start_menu_frame = tk.Frame(self)
        self.frameList.append(self.start_menu_frame)
        #Slider from 3 to 10
        # Label that says "Choose a board size"
        self.board_size_label = tk.Label(self.start_menu_frame, text="Choose a board size")
        self.board_size_label.grid(row=0, column=0, padx=0, pady=0)
        self.board_size_slider = tk.Scale(self.start_menu_frame, from_=3, to=10, orient=HORIZONTAL, label="")
        self.board_size_slider.grid(row=1, column=0, padx=0, pady=0)
        #Game Mode
        self.game_mode_var = tk.StringVar()
        self.game_mode_var.set("None")
        self.game_mode_label = tk.Label(self.start_menu_frame, text="Choose a Game Mode")
        self.game_mode_label.grid(row=2, column=0, padx=0, pady=0)
        # help menu question mark
        self.help_button = tk.Button(self.start_menu_frame, text=" ? ", command=self.buildHelpMenu)
        self.help_button.grid(row=2, column=1, padx=0, pady=0)

        self.game_mode_radio1 = tk.Radiobutton(self.start_menu_frame, text="Simple", variable=self.game_mode_var, value="Simple")
        self.game_mode_radio1.grid(row=3, column=0, padx=0, pady=0)
        self.game_mode_radio2 = tk.Radiobutton(self.start_menu_frame, text="General", variable=self.game_mode_var, value="General")
        self.game_mode_radio2.grid(row=4, column=0, padx=0, pady=0)


        # Get board size slider value
        x = self.board_size_slider.get()
        # Get board game mode
        y = self.game_mode = self.game_mode_var.get()
        #Start Button
        self.start_button = tk.Button(self.start_menu_frame, text="Start", command=self.buildMainGame)
        self.start_button.grid(row=6, column=0, padx=0, pady=0)
        self.start_menu_frame.pack()


    def buildHelpMenu(self):
            #create new window
            self.help_window = tk.Toplevel(self)
            self.help_window.title("Help")
            self.help_window.geometry("225x325")
            self.help_window.iconbitmap( 'SOS.ico')
            
            # Help Menu Frame
            self.help_menu_frame = tk.Frame(self.help_window)
            self.help_menu_frame.pack()
            self.frameList.append(self.help_menu_frame)
            # Help Menu Text
            self.help_menu_text = tk.Label(self.help_menu_frame, text="SOS Help Menu")
            self.help_menu_text.grid(row=0, column=0, padx=0, pady=0)
            # Simple Game Mode Help Label
            self.simple_game_mode_help_label = tk.Label(self.help_menu_frame, text="Simple Game Mode Instructions")
            self.simple_game_mode_help_label.grid(row=1, column=0, padx=0, pady=0)
            # make text wrap
            self.seperator = ttk.Separator(self.help_menu_frame, orient=HORIZONTAL)
            self.seperator.grid(row=2, column=0, padx=0, pady=0)
            self.simple_game_mode_help_text = tk.Label(self.help_menu_frame, text="In a simple game, users take turn placing down their S or O token on the board. If a player places down a token and creates a SOS in any direction, they get a point. The winner of the game is the first player to make an SOS.", wraplength=200)
            self.simple_game_mode_help_text.grid(row=2, column=0, padx=0, pady=0)

            # General Game Mode Help Label
            self.general_game_mode_help_label = tk.Label(self.help_menu_frame, text="General Game Mode Instructions")
            self.general_game_mode_help_label.grid(row=3, column=0, padx=0, pady=0)
            # make text wrap
            self.seperator = ttk.Separator(self.help_menu_frame, orient=HORIZONTAL)
            self.seperator.grid(row=4, column=0, padx=0, pady=0)
            self.general_game_mode_help_text = tk.Label(self.help_menu_frame, text="In a general game, users take turn placing down their S or O token on the board. When all the positions on the board have been filled by a token, the winner of the game is whoever made the most SOS's and obtained the most points.", wraplength=200)
            self.general_game_mode_help_text.grid(row=4, column=0, padx=0, pady=0)



            # Help Menu Close Button
            self.help_menu_close_button = tk.Button(self.help_menu_frame, text="Close", command=self.help_window.destroy)
            self.help_menu_close_button.grid(row=5, column=0, padx=0, pady=0)


    def buildMainGame(self):
        self.gameStarted = True
        # Delete Start Menu
        self.board_size = self.board_size_slider.get()

        self.board.updateBoardSize(str(self.board_size))
        # Get game mode
        if self.game_mode_var.get() == "None":
            self.game_mode_var.set("Simple")
        # delete all frames in frameList
        for frame in self.frameList:
            frame.destroy()

        # Create frame for Board Title and widgets
        self.board_frame = tk.Frame(self)
        self.board_frame.pack(pady=10)
        self.frameList.append(self.board_frame)
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
        self.frameList.append(self.game_mode_frame)
        #Include 2 radio buttons one labeled simple and one labeled general
        #And reset the board when the radio button is clicked
        self.game_mode_var.set(self.game_mode_var.get())
        self.game_mode_frame.pack(pady=10)
        self.game_mode_label = tk.Label(self.game_mode_frame, text="Game Mode: ")
        self.game_mode_label.grid(row=0, column=0, padx=0, pady=0)
        self.game_mode_simple = tk.Radiobutton(self.game_mode_frame, text="Simple", variable=self.game_mode_var, value="Simple", command=self.reset)
        self.game_mode_simple.grid(row=0, column=1, padx=0, pady=0)
        self.game_mode_general = tk.Radiobutton(self.game_mode_frame, text="General", variable=self.game_mode_var, value="General", command=self.reset)
        self.game_mode_general.grid(row=0, column=2, padx=0, pady=0)
        #Create frame for buttons
        self.frame = tk.Frame(self)
        self.frame.size = 1
        self.frame.pack(pady=10)
        self.frameList.append(self.frame)


        #Create nxn grid of buttons in frame
        for row in range(self.board_size):
            for column in range(self.board_size):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=2)
                button = ttk.Button(self.frame,text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)



        #Create controls frame under buttons
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=5)
        self.frameList.append(self.controls_frame)
        #Create Player 1 and Player 2 labels
        self.player1_label = tk.Label(self.controls_frame, text="Player 1", font=("Arial", 10))
        self.player1_label.grid(row=0, column=0, padx=10, pady=10)
        #Create 2 Radio Buttons for Player 1
        self.player1_var = tk.StringVar()
        self.player1_var.set("S")
        self.player1_x = tk.Radiobutton(self.controls_frame, text="S", variable=self.player1_var, value="S")
        self.player1_x.grid(row=1, column=0, padx=10, pady=10)
        self.player1_o = tk.Radiobutton(self.controls_frame, text="O", variable=self.player1_var, value="O")
        self.player1_o.grid(row=2, column=0, padx=10, pady=10)
        self.player2_label = tk.Label(self.controls_frame, text="Player 2", font=("Arial", 10))
        # Create 2 Radio Buttons for Player 2
        self.player2_var = tk.StringVar()
        self.player2_var.set("S")
        self.player2_x = tk.Radiobutton(self.controls_frame, text="S", variable=self.player2_var, value="S")
        self.player2_x.grid(row=1, column=1, padx=10, pady=10)
        self.player2_o = tk.Radiobutton(self.controls_frame, text="O", variable=self.player2_var, value="O")
        self.player2_o.grid(row=2, column=1, padx=10, pady=10)
        self.player2_label.grid(row=0, column=1, padx=10, pady=10)
        # Reset Board
        self.reset_button = tk.Button(self.controls_frame,text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=10, padx=0, pady=0)

        #upate board geometry
        self.boardWidth, self.boardHeight = self.board.getWindowSize(self.board_size)
        self.board.updateGameMode(self.game_mode_var.get())
        self.geometry(str(self.boardWidth) + "x" + str(self.boardHeight))


    def updateCurrentPlayerText(self):
        #Update Current Player Text
        self.CurrentPlayerLabel.config(text="Playing: Player " + str(self.Player))


    def reset(self):
        #Reset Board
        #Delete all buttons
        for widget in self.frame.winfo_children():
            widget.destroy()
        #Create new buttons
        for row in range(self.board_size):
            for column in range(self.board_size):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=2)
                # Add blue background to buttons
                button = ttk.Button(self.frame,text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)
        #Reset Player to 1
        self.Player = 1
        self.updateCurrentPlayerText()
        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=10, padx=0, pady=0)
        self.board.resetBoard(self.board_size)
        self.boardWidth, self.boardHeight = self.board.getWindowSize(self.board_size)
        self.board.updateGameMode(self.game_mode_var.get())
        self.geometry(str(self.boardWidth) + "x" + str(self.boardHeight))

        
        

    def clicked(self):

        #Get Clicked Button
        button = self.focus_get()
        # Change buttons type to not be a TButton

        row = button.grid_info()["row"]
        column = button.grid_info()["column"]

        self.gameMode = self.game_mode_var.get()
        self.board.gameMode = self.gameMode
        if self.Player == 1 and self.board.getPiece(row,column) == "":
            token = self.player1_var.get()
            #Change Button Text to Player 1's Choice
            button.config(text=self.player1_var.get())
            self.board.placePiece(row, column, token, self.Player)
            if token == "S":
                self.board.checkSPlacedPoint(row, column, self.Player)
            else:
                self.board.checkOPlacedPoint(row, column, self.Player)



            #Change Player to 2

            #update button text color to be red
        elif self.Player == 2 and self.board.getPiece(row,column) == "":
            token = self.player2_var.get()
            #Change Button Text to Player 2's Choice
            button.config(text=self.player2_var.get())
            #Change Player to 1
            self.board.placePiece(row, column, self.player2_var.get(), self.Player)
            if token == "S":
                self.board.checkSPlacedPoint(row, column, self.Player)
            else:
                self.board.checkOPlacedPoint(row, column, self.Player)
        else:
            messagebox.showerror("Error", "Button already clicked")

        if self.gameMode == "Simple":
            if self.board.checkForSimpleWin():
                messagebox.showinfo("Winner", "Player " + str(self.Player) + " Wins!")
                self.reset()
        else:
            if self.board.noOpenSpaces():
                winner = self.board.getGeneralWinner()
                messagebox.showinfo("Winner", "Player " + str(winner) + " Wins!")
                self.reset()

        if self.Player == 1:
            self.Player = 2
        else:
            self.Player = 1
        self.updateCurrentPlayerText()

    def update_board_size(self, event):
        tempBoardSize = self.board_size_entry.get()
        self.board_size, errorMessage = self.board.updateBoardSize(tempBoardSize)
        if errorMessage != "":
            messagebox.showerror("Error", errorMessage)
        self.reset()