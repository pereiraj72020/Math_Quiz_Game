from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Heading (row 1)
        self.my_label = Label(self.start_frame, text="This is my text",
                              font="Arial 14 bold")
        self.my_label.grid(row=1, pady=10)

        # Math Heading (row 1)
        self.my_button = Button(self.start_frame, text="Click Me",
                                command=lambda: self.something, font="Arial 14 bold")
        self.my_button.grid(row=2, pady=10)


    def something(self):
        my_label.config(text="This is new text!!")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    something = Start(root)
    root.mainloop()
