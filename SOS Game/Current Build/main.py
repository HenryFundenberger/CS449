
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
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'white', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active','black')], forground=[('active','white')])
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
        self.board = Board(self.board_size)

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
        self.game_mode_label.grid(row=0, column=0, padx=0, pady=0)
        self.game_mode_simple = tk.Radiobutton(self.game_mode_frame, text="Simple", variable=self.game_mode_var, value="simple", command=self.reset)
        self.game_mode_simple.grid(row=0, column=1, padx=0, pady=0)
        self.game_mode_general = tk.Radiobutton(self.game_mode_frame, text="General", variable=self.game_mode_var, value="general", command=self.reset)
        self.game_mode_general.grid(row=0, column=2, padx=0, pady=0)



        #Create frame for buttons
        self.frame = tk.Frame(self)
        self.frame.size = 1
        self.frame.pack(pady=10)

        #Create 8x8 grid of buttons in frame
        for row in range(8):
            for column in range(8):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=2)
                button = ttk.Button(self.frame,text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)


        #Create controls frame under buttons
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=5)

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


    def updateCurrentPlayerText(self):
        #Update Current Player Text
        if self.Player == 1:
            self.CurrentPlayerLabel.config(text="Playing: Player 1")
        else:
            self.CurrentPlayerLabel.config(text="Playing: Player 2")

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
        self.reset_button = tk.Button(self.controls_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=10, padx=0, pady=0)
        self.board.resetBoard(self.board_size)


    def clicked(self):
        #Get Clicked Button
        button = self.focus_get()
        row = button.grid_info()["row"]
        column = button.grid_info()["column"]

        #Board Object print board method



        #Current Player
        player = self.Player
        self.gameMode = self.game_mode_var.get()
        print(self.gameMode)
        print("=====================================")
        x = self.board.getPiece(row, column)
        print(x)
        print("=====================================")
        if player == 1 and self.board.getPiece(row,column) == "":
            #Change Button Text to Player 1's Choice
            button.config(text=self.player1_var.get())
            self.board.placePiece(row, column, self.player1_var.get(), player)
            #Change Player to 2
            self.Player = 2
            self.updateCurrentPlayerText()
            #update button text color to be red
        elif player == 2 and button["text"] == " ":
            #Change Button Text to Player 2's Choice
            button.config(text=self.player2_var.get())
            #Change Player to 1
            self.board.placePiece(row, column, self.player2_var.get(), player)
            self.Player = 1
            self.updateCurrentPlayerText()
        else:
            messagebox.showerror("Error", "Button already clicked")
        
        print(self.board.getPiece(row, column))


    def update_board_size(self, event):
        # If board size > 10, set to 10
        # Display pop up error message
        if int(self.board_size_entry.get()) > 10:
            messagebox.showerror("Error", "Board sizes much greater than 10 cause errors, please enter 10 or less")
            self.board_size = 10
        elif int(self.board_size_entry.get()) < 3:
            messagebox.showerror("Error", "Board size must be greater than or equal to 3")
            self.board_size = 3
        else:
            self.board_size = int(self.board_size_entry.get())

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
        self.board.resetBoard(self.board_size)






#Main SECTION
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
