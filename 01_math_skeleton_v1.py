from tkinter import *
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

        # Amount of questions (row 2)
        self.question_amount = Amount(self.start_frame,
                                      "How many Questions? {}".format(questions))
        self.question_amount.grid(row=3)

        # Addition button (row 3)
        self.addition_button = Addition(self.start_frame, text='col', bg='gray25',
                                        activebackground='cyan')
        self.addition_button.grid(row=4)

        # Subtraction button (row 4)
        self.subtraction_button = Subtraction(self.start_frame, text='col', bg='gray25',
                                              activebackground='cyan')
        self.subtraction_button.grid(row=5)

        # Multiplication button (row 5)
        self.multiplication_button = Multiplication(self.start_frame, text='col', bg='gray25',
                                                    activebackground='cyan')
        self.multiplication_button.grid(row=6)

        # Division button (row 6)
        self.division_button = Division(self.start_frame, text='col', bg='gray25,',
                                        activebackground='cyan')
        self.division_button.grid(row=7)

        # Play Button (row 7)
        self.play_button = Play(text="Play... ",
                                command=lambda: self.to_game((1)))
        self.play_button.grid(row=2, pady=10)


    def to_game(self, button):
        starting_questions = self.start_amount_entry.get()
        Game(self, button, starting_questions)


class Game:
    def __init__(self, partner, button, starting_questions):
        print(button)
        print(starting_questions)
        
        # disable buttons
        partner.addition_button.config(state=DISABLED)
        partner.subtraction_button.config(state=DISABLED)
        partner.multiplication_button.config(state=DISABLED)
        partner.division_button.config(state=DISABLED)

        # initialise variables
        self.questions = IntVar()

        # Set starting questions to amount entered by user
        self.questions.set(starting_questions)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   )







# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(parent=DISABLED)
    root.mainloop()

        
        



