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





#Main SECTION TEST FUNCTIONS
#---------------------------------------------------------------

def test_ResizeBoard():
    app = NewTestApp()
    app.after(1000, app.test_ResizeBoard())
    app.after(2000, app.destroy())
    app.mainloop()
    assert app.board_size == 3 and app.buttonTest == "S"



#Main SECTION
#-----------------------------------------------------------------------------------------------------------------------



