from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # GUI Setup
        self.game_box = Toplevel()

        # Set Initial questions to zero
        self.starting_question = IntVar()
        self.starting_question.set(0)

        # if users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)

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

        # Number input text (row 2)
        self.number_input_text = Label(self.start_frame, text="Enter numbers between...",
                                       justify=LEFT, bg="#ffafaf", fg="maroon",
                                       font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.number_input_text.grid(row=2, pady=10)

        # Number input_1 (row 3)
        self.number_input_1 = Entry(self.start_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_1.grid(row=3, column=0, pady=10)

        # 'And' between Number input_1 and input_2 (row 3)
        self.and_1 = Label(self.start_frame, text="And",
                           justify=LEFT, bg="#ffafaf", fg="maroon",
                           font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.and_1.grid(row=3, column=1, padx=5, pady=10)

        # Number input_2 (row 3)
        self.number_input_2 = Entry(self.start_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_2.grid(row=3, column=2, pady=10)

        # Amount of questions text (row 3)
        self.question_text = Label(self.start_frame, text="How many questions?",
                                   justify=LEFT, bg="#ffafaf", fg="maroon",
                                   font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.question_text.grid(row=3, pady=10)

        # Amount of questions Entry Box (row 4)
        self.question_amount = Entry(self.start_frame, width=20,
                                     font="Arial 14 bold", justify=CENTER)
        self.question_amount.grid(row=4, pady=10)

        # button frame (row 6)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=6)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Addition button (row 4)
        self.addition_button = Button(self.start_frame, text='Addition', bg='gray25', font=button_font,
                                      command=lambda: self.to_game(1), activebackground='cyan')
        self.addition_button.grid(row=4)

        # Subtraction button (row 5)
        self.subtraction_button = Button(self.start_frame, text='Subtraction', bg='gray25', font=button_font,
                                         command=lambda: self.to_game(2), activebackground='cyan')
        self.subtraction_button.grid(row=5)

        # Multiplication button (row 6)
        self.multiplication_button = Button(self.start_frame, text='Multiplication', bg='gray25', font=button_font,
                                            command=lambda: self.to_game(3), activebackground='cyan')
        self.multiplication_button.grid(row=6)

        # Division button (row 7)
        self.division_button = Button(self.start_frame, text='Division', bg='gray25', font=button_font,
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
        # Retrieve starting questions
        starting_questions = self.starting_question.get()

        # self.start_frame.destroy()
        self.start_frame.destroy()
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
    root.title("Math Quiz Game")
    something = Start(root)
    root.mainloop()
