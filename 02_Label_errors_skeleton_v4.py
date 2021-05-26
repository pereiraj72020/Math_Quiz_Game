from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get user's numbers
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Heading (row 1)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=1)

        # Initial Instructions (row 2)
        self.math_instructions = Label(self.start_frame,
                                       font="Arial 10 italic",
                                       text="Enter in your selected two integers and the amount "
                                            "of questions that is going to be answered. "
                                            "Then select either addition, subtraction, multiplication "
                                            "or division when finished doing the following to start "
                                            "the game. ",
                                       wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=2)

        # Number input text (row 3)
        self.number_input_text = Label(self.start_frame, text="Enter numbers between...",
                                       justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                       relief="groove",
                                       font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.number_input_text.grid(row=3, pady=10)

        # Number input frame (row 4)
        self.number_input_frame = Frame(self.start_frame)
        self.number_input_frame.grid(row=4)

        # Number input_1 (row 4)
        self.number_input_1 = Entry(self.number_input_frame, width=10,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_1.grid(row=0, column=0, pady=10)

        # 'And' between Number input_1 and input_2 (row 4)
        self.and_1 = Label(self.number_input_frame, text="And",
                           justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                           relief="groove",
                           font="Arial 10 bold", wrap=225, padx=10, pady=3)
        self.and_1.grid(row=0, column=1, padx=5, pady=10)

        # Number input_2 (row 4)
        self.number_input_2 = Entry(self.number_input_frame, width=10,
                                    font="Arial 14 bold", justify=CENTER)
        self.number_input_2.grid(row=0, column=2, pady=10)

        # Amount error label (row 5)
        self.amount_error_label_1 = Label(self.number_input_frame, fg="maroon",
                                          text="", font="Arial 10 bold", wrap=275,
                                          justify=LEFT)
        self.amount_error_label_1.grid(row=5, columnspan=2, pady=5)

        # Amount of questions text (row 5)
        self.question_text = Label(self.start_frame, text="How many questions?",
                                   justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                   relief="groove",
                                   font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.question_text.grid(row=5, pady=10)

        # Question amount Frame
        self.question_amount_frame = Frame(self.start_frame, width=200)
        self.question_amount_frame.grid(row=6)

        # Amount of questions Entry Box (row 6)
        self.question_amount = Entry(self.question_amount_frame, width=20,
                                     font="Arial 14 bold", justify=CENTER)
        self.question_amount.grid(row=0, pady=10, column=0)

        # Amount error label (row 5)
        self.amount_error_label_2 = Label(self.question_amount_frame, fg="maroon",
                                          text="", font="Arial 10 bold", wrap=275,
                                          justify=LEFT)
        self.amount_error_label_2.grid(row=5, columnspan=2, pady=5)

        # button frame (row 7)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=7)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Addition button (row 7)
        self.addition_button = Button(self.button_frame, text='Addition', bg="#008000", font=button_font,
                                      fg="white", command=self.check_errors, activebackground="#FFA500")

        self.addition_button.grid(row=0, column=0)

        # Subtraction button (row 7)
        self.subtraction_button = Button(self.button_frame, text='Subtraction', bg="#008000", font=button_font,
                                         fg="white", command=self.check_errors, activebackground="#FFA500")
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=10)

        # Multiplication button (row 7)
        self.multiplication_button = Button(self.button_frame, text='Multiplication', bg="#008000", font=button_font,
                                            fg="white", command=self.check_errors, activebackground="#FFA500")
        self.multiplication_button.grid(row=0, column=2, padx=5, pady=10)

        # Division button (row 7)
        self.division_button = Button(self.button_frame, text='Division', bg="#008000", font=button_font,
                                      fg="white", command=self.check_errors, activebackground="#FFA500")
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
        questions = self.question_amount.get()

        num_1 = self.number_input_1.get()
        num_2 = self.number_input_2.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"
        error_feedback = ""

        # Change background to white (for testing purposes) ...
        self.number_input_1.config(bg="white")
        self.number_input_2.config(bg="white")
        self.amount_error_label_1.config(text="")
        self.question_amount.config(bg="white")
        self.amount_error_label_2.config(text="")

        try:
            questions = int(questions)

            if questions < 1:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can enter is 1"
            elif questions > 20:
                has_errors = "yes"
                error_feedback = "Sorry, the most you can enter is 20"
            elif num_1 > num_2:
                has_errors = "yes"
                error_feedback = "Num 1 is more than Num 2"
            elif num_1 < 1:
                has_errors = "yes"
                error_feedback = "Num 1 is less than 1"
            elif num_2 > 12:
                has_errors = "yes"
                error_feedback = "Num 2 is more than 12"
            else:
                # Enable all buttons
                self.addition_button.config(state=NORMAL)
                self.subtraction_button.config(state=NORMAL)
                self.multiplication_button.config(state=NORMAL)
                self.division_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.question_amount.config(bg=error_back)
            self.amount_error_label_2.config(text=error_feedback)
        else:
            self.number_input_1.config(bg=error_back)
            self.number_input_2.config(bg=error_back)
            self.amount_error_label_1.config(text=error_feedback)

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

        help_text = "Type in two numbers that signify all numbers between and itself to answer " \
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
    def __init__(self, partner, button, questions):
        print(button)
        print(questions)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    something = Start(root)
    root.mainloop()
