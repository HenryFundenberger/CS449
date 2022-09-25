from contextlib import redirect_stderr
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("600x300")
        self.resizable(True, True)
        self.create_widgets()
    def create_widgets(self):
       #Create label in center of window
        self.label = tk.Label(self, text="SOS", font=("Arial", 20))
        self.label.pack(pady=10)
        #Create frame for buttons
        self.frame = tk.Frame(self)
        self.frame.size = 3
        self.frame.pack(pady=10)
        #Create 8x8 grid of buttons in frame
        for row in range(3):
            for column in range(3):
                #Remove Space between buttons
                self.frame.columnconfigure(column, weight=1)
                button = ttk.Button(self.frame, text=" ", width=3, command=self.clicked)
                button.grid(row=row, column=column, padx=0, pady=0)
        #Create controls frame under buttons
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=5)
        #Create Player 1 and Player 2 labels
        self.player1_label = tk.Label(self.controls_frame, text="Player 1", font=("Arial", 10))
        self.player1_label.grid(row=0, column=0, padx=10, pady=10)
        #Create 2 Radio Buttons for Player 1
        self.player1_var = tk.StringVar()
        self.player1_var.set("X")
        self.player1_x = tk.Radiobutton(self.controls_frame, text="S", variable=self.player1_var, value="S")
        self.player1_x.grid(row=2, column=0, padx=10, pady=10)
        self.player1_o = tk.Radiobutton(self.controls_frame, text="O", variable=self.player1_var, value="O")
        self.player1_o.grid(row=3, column=0, padx=10, pady=10)
        # add check button to enable/disable player 1
        self.player1_check = tk.Checkbutton(self.controls_frame, text="Player 1", variable=self.player1_var)
        self.player1_check.grid(row=1, column=0, padx=0, pady=0)
        self.player2_label = tk.Label(self.controls_frame, text="Player 2", font=("Arial", 10))
        # Create 2 Radio Buttons for Player 2
        self.player2_var = tk.StringVar()
        self.player2_var.set("O")
        self.player2_x = tk.Radiobutton(self.controls_frame, text="S", variable=self.player2_var, value="S")
        self.player2_x.grid(row=2, column=1, padx=10, pady=10)
        self.player2_o = tk.Radiobutton(self.controls_frame, text="O", variable=self.player2_var, value="O")
        self.player2_o.grid(row=3, column=1, padx=10, pady=10)
        self.player2_label.grid(row=0, column=1, padx=10, pady=10)
        # Add Check button to enable/disable player 2
        self.player2_check = tk.Checkbutton(self.controls_frame, text="Player 2", variable=self.player2_var)
        self.player2_check.grid(row=1, column=1, padx=0, pady=0)
        # Draw Rectange
        self.canvas = tk.Canvas(self, width=600, height=300)
        self.canvas.pack()
        blueRect = self.canvas.create_rectangle(0, 0, 600, 10, fill="blue")
        redRect = self.canvas.create_rectangle(0, 0, 600, 10, fill="red")

        #Translate blue rectangle
        self.canvas.move(blueRect, 0, 10)
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    

    def clicked(self):
        #Get Clicked Button
        button = self.focus_get()
        #Current Player
        player = self.player1_var.get()

        #Change Button Text to X or O
        if button["text"] == " ":
            if player == "X":
                button["text"] = "X"
            else:
                button["text"] = "O"
        else:
            messagebox.showerror("Error", "Button already clicked")
        
        

        
    

        


    def button_clicked(self):
        # Change Button text to X or O
        button = self.focus_get()
        

