from tkinter import *
from functools import partial  # To prevent unwated windows
import random


class Start:
    def __init__(self, parent):
        check_input = 1
        check_input_2 = 12
        questions = []

        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # GUI Setup
        self.game_box = Toplevel()

        # if users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Math Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=1)

        # Initial Instructions (row 1)
        self.math_instructions = Label(self.start_frame,
                                       font="Arial 10 italic",
                                       text="Enter in your selected two integers and the amount"
                                       "of questions that is going to be answered. Select either"
                                       "addition, subtraction, multiplication or division. Then"
                                       "<click> Start when finished doing the following.")

        # Entry box... (row 2)
        self.start_amount_entry = Entry(self.start_frame)
        self.start_amount_entry.grid(row=2)

        # Amount of questions (row 3)
        self.question_amount = Entry(self.start_frame,
                                     "How many Questions? {}".format(questions))
        self.question_amount.grid(row=3)

        # Addition button (row 4)
        self.addition_button = Button(self.start_frame, text='Addition', bg='gray25',
                                      command=lambda: self.to_game(1), activebackground='cyan')
        self.addition_button.grid(row=4)

        # Subtraction button (row 5)
        self.subtraction_button = Button(self.start_frame, text='Subtraction', bg='gray25',
                                         command=lambda: self.to_game(2), activebackground='cyan')
        self.subtraction_button.grid(row=5)

        # Multiplication button (row 6)
        self.multiplication_button = Button(self.start_frame, text='Multiplication', bg='gray25',
                                            command=lambda: self.to_game(3), activebackground='cyan')
        self.multiplication_button.grid(row=6)

        # Division button (row 7)
        self.division_button = Button(self.start_frame, text='Division', bg='gray25',
                                      command=lambda: self.to_game(4), activebackground='cyan')
        self.division_button.grid(row=7)

        # Start button (row 8)
        self.start_button = Button(self.start_frame, text='Start', bg="#FFFF00",
                                   command=lambda: self.to_game(5))
        self.start_button.grid(row=8)

        # Help/Rules Button (row 9)
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=9, column=0)

        # Quit Button (row 9)
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=9, column=1)

    def to_game(self, button):
        starting_questions = self.start_amount_entry.get()
        Game(self, button, starting_questions)

    def to_quit(self):
        root.destroy()


class Game:
    def __init__(self, partner, button, starting_questions):
        print(button)
        print(starting_questions)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(parent=DISABLED)
    root.mainloop()
