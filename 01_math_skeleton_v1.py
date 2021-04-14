from tikinter import *
from functools import partial   # To prevent unwated windows
import random


class Start:
    def __init__(self, parent):

        check_input = []
        check_input_2 = []
        questions = []

        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=1)

        # Entry box... (row 1)
        self.start_amount_entry = Entry(self.start_frame,
                                        "Numbers between {} and {}".format(check_input, check_input_2))
        self.start_amount_entry.grid(row=2)

        # Amount of questions
        self.question_amount = Amount(self.start_frame,
                                      "How many Questions? {}".format(questions))
