from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set Initial questions to zero
        self.starting_question = IntVar()
        self.starting_question.set(0)

        # Math Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=0)

        # Initial Instructions (row 1)
        self.math_instructions = Label(self.start_frame,
                                       font="Arial 10 italic",
                                       text="Enter in your selected two integers and the amount "
                                            "of questions that is going to be answered. "
                                            "Then select either addition, subtraction, multiplication "
                                            "or division when finished doing the following to start "
                                            "the game. ",
                                       wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=1)

        # Number input text (row 2)
        self.number_input_text = Label(self.start_frame, text="Enter numbers between...",
                                       justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                       relief="groove",
                                       font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.number_input_text.grid(row=2, pady=10)

        # Number input frame (row 3)
        self.number_input_frame = Frame(self.start_frame)
        self.number_input_frame.grid(row=3)

        # Number input_1 (row 3)
        self.number_input_1 = Entry(self.number_input_frame, width=10,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_1.grid(row=0, column=0, pady=10)

        # 'And' between Number input_1 and input_2 (row 3)
        self.and_1 = Label(self.number_input_frame, text="And",
                           justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                           relief="groove",
                           font="Arial 10 bold", wrap=225, padx=10, pady=3)
        self.and_1.grid(row=0, column=1, padx=5, pady=10)

        # Number input_2 (row 3)
        self.number_input_2 = Entry(self.number_input_frame, width=10,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_2.grid(row=0, column=2, pady=10)

        # Amount of questions text (row 4)
        self.question_text = Label(self.start_frame, text="How many questions?",
                                   justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                   relief="groove",
                                   font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.question_text.grid(row=4, pady=10)

        # Amount of questions Entry Box (row 5)
        self.question_amount = Entry(self.start_frame, width=20,
                                     font="Arial 14 bold", justify=CENTER)
        self.question_amount.grid(row=5, pady=10)

        # button frame (row 6)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=6)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Addition button (row 6)
        self.addition_button = Button(self.button_frame, text='Addition', bg="#008000", font=button_font,
                                      fg="white", activebackground="#FFA500")
        self.addition_button.grid(row=0, column=0)

        # Subtraction button (row 6)
        self.subtraction_button = Button(self.button_frame, text='Subtraction', bg="#008000", font=button_font,
                                         fg="white", activebackground="#FFA500")
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=10)

        # Multiplication button (row 6)
        self.multiplication_button = Button(self.button_frame, text='Multiplication', bg="#008000", font=button_font,
                                            fg="white", activebackground="#FFA500")
        self.multiplication_button.grid(row=0, column=2, padx=5, pady=10)

        # Division button (row 6)
        self.division_button = Button(self.button_frame, text='Division', bg="#008000", font=button_font,
                                      fg="white" ,activebackground="#FFA500")
        self.division_button.grid(row=0, column=3, pady=10)

        # Help_Quit frame (row 7)
        self.help_quit_frame = Frame(self.start_frame)
        self.help_quit_frame.grid(row=7)

        # Help/Rules Button (row 7)
        self.help_button = Button(self.help_quit_frame, text="Help/Rules", bg="#808080",
                                  fg="white", font=button_font, width=10)
        self.help_button.grid(row=0, column=0)

        # Quit Button (row 7)
        self.quit_button = Button(self.help_quit_frame, text="Quit", bg="#660000",
                                  fg="white", font=button_font, width=10)
        self.quit_button.grid(row=0, column=1, padx=5, pady=10)

    def to_game(self, button):
        # Retrieve starting questions
        starting_questions = self.starting_question.get()

        # self.start_frame.destroy()
        self.start_frame.destroy()
        Game(self, button, starting_questions)


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
