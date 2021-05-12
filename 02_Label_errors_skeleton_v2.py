from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

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

        # Amount of questions text (row 5)
        self.question_text = Label(self.start_frame, text="How many questions?",
                                   justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                   relief="groove",
                                   font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.question_text.grid(row=5, pady=10)

        # Amount of questions Entry Box (row 6)
        self.question_amount = Entry(self.start_frame, width=20,
                                     font="Arial 14 bold", justify=CENTER)
        self.question_amount.grid(row=6, pady=10)

        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=4)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.entry_error_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4, column=0)

        # Error Message Labels (initially blank, row 4)
        self.amount_error_label = Label(self.entry_error_frame, text="", fg="maroon")
        self.amount_error_label.grid(row=4, column=2)

        # button frame (row 7)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=7)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Addition button (row 7)
        self.addition_button = Button(self.button_frame, text='Addition', bg="#008000", font=button_font,
                                      fg="white", activebackground="#FFA500")
        self.addition_button.grid(row=0, column=0)

        # Subtraction button (row 7)
        self.subtraction_button = Button(self.button_frame, text='Subtraction', bg="#008000", font=button_font,
                                         fg="white", activebackground="#FFA500")
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=10)

        # Multiplication button (row 7)
        self.multiplication_button = Button(self.button_frame, text='Multiplication', bg="#008000", font=button_font,
                                            fg="white", activebackground="#FFA500")
        self.multiplication_button.grid(row=0, column=2, padx=5, pady=10)

        # Division button (row 7)
        self.division_button = Button(self.button_frame, text='Division', bg="#008000", font=button_font,
                                      fg="white" ,activebackground="#FFA500")
        self.division_button.grid(row=0, column=3, pady=10)

        # Help_Quit frame (row 8)
        self.help_quit_frame = Frame(self.start_frame)
        self.help_quit_frame.grid(row=8)

        # Help/Rules Button (row 8)
        self.help_button = Button(self.help_quit_frame, text="Help/Rules", bg="#808080",
                                  fg="white", font=button_font, width=10,
                                  command=self.to_help)
        self.help_button.grid(row=0, column=0)

        # Quit Button (row 8)
        self.quit_button = Button(self.help_quit_frame, text="Quit", bg="#660000",
                                  fg="white", font=button_font, width=10,
                                  command=self.to_quit)
        self.quit_button.grid(row=0, column=1, padx=5, pady=10)

    def check_errors(self):
        starting_question = self.number_input_text.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"
        error_feedback = ""

        try:
            starting_question = int(starting_question)

            if starting_question < 1:
                has_errors = "yes"
                error_feedback = "Sorry, the least amount of rounds is 1"
            elif starting_question > 50:
                has_errors = "yes"
                error_feedback = "Sorry, the most amount of rounds is 50"
            elif starting_question:
                self.addition_button.config(state=NORMAL)
                self.subtraction_button.config(state=NORMAL)
                self.multiplication_button.config(state=NORMAL)
                self.division_button.config(state=NORMAL)
            else:
                self.addition_button.config(state=DISABLED)
                self.subtraction_button.config(state=DISABLED)
                self.multiplication_button.config(state=DISABLED)
                self.division_button.config(state=DISABLED)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number"

        if has_errors == "yes":
            self.number_input_1.config(bg=error_back)
            self.number_input_1.config(text=error_feedback)
            self.number_input_2.config(bg=error_back)
            self.number_input_2.config(text=error_feedback)
        else:
            self.addition_button.config(state=NORMAL)
            self.subtraction_button.config(state=NORMAL)
            self.multiplication_button.config(state=NORMAL)
            self.division_button.config(state=NORMAL)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="Type in two numbers that signify all numbers between and itself to answer " \
                  ". Type in the amount of rounds you want to play. Then choose either addition,  " \
                  "subtraction, multiplication or division to start the game.\n\n " \
                  "When you enter the play area, type in appropriate integers after the equals sign " \
                  "to answer the question. Round limit you have input from the beginning of the " \
                  "has been reached the play area will stop and say finished.\n\n " \
                  "The stats of the questions answered will be added to the Game Stats.\n\n " \
                  "Which then shows the amount of questions correct and incorrect. " \
                  " Questions correct {} / Rounds {}, Questions incorrect {}."

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


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
