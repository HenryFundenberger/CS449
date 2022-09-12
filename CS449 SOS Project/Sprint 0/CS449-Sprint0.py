import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add Title Label
        self.title = tk.Label(self, text="CS449 Sprint 0")
        self.title.pack(side="top")

        # Add Blue Rectangle
        self.blue_rect = tk.Canvas(self, width=200, height=10, bg="blue")
        self.blue_rect.pack(side="top")

        self.red_rect = tk.Canvas(self, width=200, height=10, bg="red")
        self.red_rect.pack(side="top")

        # Add 3 Check Boxes
        self.check_box = tk.Checkbutton(self, text="Check Box")
        self.check_box.pack(side="top")

        self.check_box = tk.Checkbutton(self, text="Check Box")
        self.check_box.pack(side="top")

        self.check_box = tk.Checkbutton(self, text="Check Box")
        self.check_box.pack(side="top")

 
        # Add 2 Radio Buttons
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.radio1 = tk.Radiobutton(self, text="Radio 1", variable=self.radio_var, value=1)
        self.radio1.pack(side="top")
        self.radio2 = tk.Radiobutton(self, text="Radio 2", variable=self.radio_var, value=2)
        self.radio2.pack(side="top")



App(tk.Tk()).mainloop()
