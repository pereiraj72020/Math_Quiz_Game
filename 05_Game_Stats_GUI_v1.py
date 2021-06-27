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
                                       text="Enter in your favoured number as it "
                                            "will be shown through each question. "
                                            "Next enter an amount of questions that "
                                            "is going to be answered. Then select either "
                                            "addition, subtraction, multiplication or division "
                                            "when finished doing the following to start the game. "
                                       ,
                                       wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=2)

        # Number input text (row 3)
        self.number_input_text = Label(self.start_frame, text="Enter number...",
                                       justify=LEFT, bg="#FFFF00", fg="black", borderwidth=2,
                                       relief="groove",
                                       font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.number_input_text.grid(row=3, pady=10)

        # Number input frame (row 4)
        self.start_number_input_frame = Frame(self.start_frame)
        self.start_number_input_frame.grid(row=4)

        # Number input_1 (row 4)
        self.number_input = Entry(self.start_number_input_frame, width=20,
                                  font="Arial 14 bold", justify=CENTER)
        self.number_input.grid(row=0, column=0, pady=10)

        # Amount error label (row 3)
        self.start_amount_error_label_1 = Label(self.start_number_input_frame, fg="maroon",
                                                text="", font="Arial 10 bold", wrap=275,
                                                justify=LEFT)
        self.start_amount_error_label_1.grid(row=3, columnspan=2, pady=5)

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
        self.start_amount_error_label_2 = Label(self.question_amount_frame, fg="maroon",
                                                text="", font="Arial 10 bold", wrap=275,
                                                justify=LEFT)
        self.start_amount_error_label_2.grid(row=5, columnspan=2, pady=5)

        # button frame (row 7)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=7)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Addition button (row 7)
        self.addition_button = Button(self.button_frame, text='Addition', bg="#008000", font=button_font,
                                      fg="white", command=lambda: self.check_errors_n_button("+"),
                                      activebackground="#FFA500")
        self.addition_button.grid(row=0, column=0)

        # Subtraction button (row 7)
        self.subtraction_button = Button(self.button_frame, text='Subtraction', bg="#008000", font=button_font,
                                         fg="white", command=lambda: self.check_errors_n_button("-"),
                                         activebackground="#FFA500")
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=10)

        # Multiplication button (row 7)
        self.multiplication_button = Button(self.button_frame, text='Multiplication', bg="#008000", font=button_font,
                                            fg="white", command=lambda: self.check_errors_n_button("*"),
                                            activebackground="#FFA500")
        self.multiplication_button.grid(row=0, column=2, padx=5, pady=10)

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

    def check_errors_n_button(self, operation):
        questions = self.question_amount.get()
        num = self.number_input.get()

        # add = self.addition_button.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"
        error_feedback = ""

        # Change background to white (for testing purposes) ...
        self.number_input.config(bg="white")
        self.start_amount_error_label_1.config(text="")
        self.question_amount.config(bg="white")
        self.start_amount_error_label_2.config(text="")

        try:
            num = int(num)
            questions = int(questions)

            if num < 1:
                has_errors = "yes"
                error_feedback = "Min is 1 (Enter number...)"
            elif num > 12:
                has_errors = "yes"
                error_feedback = "Max is 12 (Enter number...)"
            elif questions < 1:
                has_errors = "yes"
                error_feedback = "Min is 1 (How many questions?)"
            elif questions > 20:
                has_errors = "yes"
                error_feedback = "Max is 20 (How many questions?)"

            else:
                # transfer to class Game
                Game(self, questions, num, operation)
                root.withdraw()

        except ValueError:
            has_errors = "yes"
            error_feedback = "Entry/s Error (blank / no decimals or text)"

        if has_errors == "yes":
            self.number_input.config(bg=error_back)
            self.start_amount_error_label_1.config(text=error_feedback)
            # elif has_errors == "yes":
            self.question_amount.config(bg=error_back)
            self.start_amount_error_label_2.config(text=error_feedback)

    def to_quit(self):
        root.withdraw()

    def to_help(self):
        get_help = Help(self)


class Game:
    def __init__(self, partner, questions, num, operation):
        print("Questions: {}".format(questions))
        print("Number being used in Play...: {}".format(num))
        print("Operation: {}".format(operation))
        print("===== Play... =====")

        # **** initialise variables ****
        self.num_questions = IntVar()
        # Set questions to amount entered by user at start of game
        self.num_questions.set(questions)

        self.num_to_use = IntVar()
        # Set number to amount entered by user at start of game
        self.num_to_use.set(num)

        self.num_operation = StringVar()
        # Set operation to amount entered by user at start of game
        self.num_operation.set(operation)

        # List for holding statistics
        self.correct_incorrect_list = []
        self.correct_list = []
        self.incorrect_list = []
        self.questions_stats = []

        print("----------")
        question_tostats = "Questions Answered: {}".format(questions)
        self.questions_stats.append(question_tostats)
        print(question_tostats)

        # GUI Setup
        self.game_box = Toplevel()

        # If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10, width=20)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Type in an appropriate integer in the box below "
                                             "after the equals sign to answer the question. "
                                             "<Click> on Next to advance to the next question. "
                                             "<Click> on Check to see if answer is correct or "
                                             "incorrect. ",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1, pady=20)

        # questions_total_frame (row 2)
        self.questions_total_frame = Frame(self.game_frame)
        self.questions_total_frame.grid(row=2)

        # push_button_frame (row 3)
        self.push_button_frame = Frame(self.game_frame)
        self.push_button_frame.grid(row=3)

        # show_questions_frame (row 4)
        self.show_questions_frame = Frame(self.game_frame)
        self.show_questions_frame.grid(row=4)

        # answer_here_frame (row 5)
        self.answer_here_frame = Frame(self.game_frame)
        self.answer_here_frame.grid(row=5)

        # user_input_frame (row 5)
        self.user_input_frame = Frame(self.game_frame)
        self.user_input_frame.grid(row=6)

        # math_quiz_number_input_frame_1(row 5)
        self.math_quiz_number_input_frame_1 = Frame(self.game_frame)
        self.math_quiz_number_input_frame_1.grid(row=7)

        # next_button_frame (row 6)
        self.next_button_frame = Frame(self.game_frame)
        self.next_button_frame.grid(row=8)

        # questions_total (row 2, column 0)
        self.questions_total = Label(self.questions_total_frame,
                                     text="", width=20, font="Arial 14 bold",
                                     justify=CENTER, relief=GROOVE)
        self.questions_total.grid(row=0, column=0, pady=0)

        # push_button_label (row 3, column 0)
        self.push_button_label = Label(self.push_button_frame, text="Push 'Next' to go to the next question ",
                                       bg="#FFA500", fg="black", borderwidth=2,
                                       relief="groove",
                                       font="Arial 11 bold", wrap=225, padx=10, pady=6)
        self.push_button_label.grid(row=0, pady=20)

        # show_questions (row 4, column 0)
        self.show_questions = Label(self.show_questions_frame, font="Arial 15 bold",
                                    fg="green", justify=CENTER, text="")
        self.show_questions.grid(row=0, column=0)

        # answer_here (row 5, column 0)
        self.answer_here = Label(self.answer_here_frame, font="Arial 11 bold",
                                 wrap=225, relief="groove", justify=LEFT,
                                 bg="#FFFF00", fg="black", borderwidth=2,
                                 text="Answer Here...", padx=10, pady=6)
        self.answer_here.grid(row=0, pady=10)

        # user_input_show_questions (row 4, column 1)
        self.user_input = Entry(self.user_input_frame, font="Arial 20 bold",
                                fg="black", justify=CENTER, width=10, state=DISABLED)
        self.user_input.grid(row=0, column=0, pady=10, ipady=10)

        # Amount error label (row 5, column 0)
        self.math_quiz_amount_error_label_1 = Label(self.math_quiz_number_input_frame_1,
                                                    font="Arial 12 bold", fg="black",
                                                    wrap=275, justify=CENTER)
        self.math_quiz_amount_error_label_1.grid(row=0, column=0, pady=20)

        # next_button (row 5, column 0)
        self.next_button = Button(self.next_button_frame, text="Next",
                                  bg="#FFA500", fg="black", width=5,
                                  font="Arial 14 bold", justify=CENTER,
                                  command=self.next_question_function)

        # bind button to <enter> (users can push enter to reveal the boxes)
        self.next_button.grid(row=0, column=0, pady=10, padx=10)

        # check_button (row 5, column 1)
        self.check_button = Button(self.next_button_frame, text="Check",
                                   bg="#008000", fg="black", width=5,
                                   font="Arial 14 bold", justify=CENTER, state=DISABLED,
                                   command=self.check_function)
        self.check_button.grid(row=0, column=1, pady=10, padx=10)

        # Help_Stats frame (row 7)
        self.help_stats_frame = Frame(self.game_frame)
        self.help_stats_frame.grid(row=9)

        # Quit frame (row 8)
        self.quit_frame = Frame(self.game_frame)
        self.quit_frame.grid(row=10)

        # Help/Rules Button (row 7)
        self.help_button = Button(self.help_stats_frame, text="Help/Rules", bg="#808080",
                                  fg="white", font="Arial 14 bold",
                                  command=self.to_help)
        self.help_button.grid(row=0, column=0)

        # Stats Button (row 7, no command yet)
        self.stats_button = Button(self.help_stats_frame, text="Game Stats...", bg="#003366",
                                   fg="white", font="Arial 14 bold",
                                   command=lambda: self.to_stats(self.questions_stats,
                                                                 self.correct_list, self.incorrect_list))
        self.stats_button.grid(row=0, column=1, padx=5, pady=10)

        # Quit Button (row 8)
        self.quit_button = Button(self.quit_frame, text="Quit", bg="#660000",
                                  fg="white", font="Arial 14 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=0, column=1, padx=5, pady=10)

    def next_question_function(self):

        self.check_button.config(state=NORMAL)
        self.user_input.config(state=NORMAL)

        # **** variables included ****
        num = self.num_to_use.get()
        operation = self.num_operation.get()
        questions = self.num_questions.get()

        # random number
        random_number = random.randint(1, 12)

        # carry over to check_function
        self.num_random = IntVar()
        self.num_random.set(random_number)

        # question down by 1
        questions -= 1

        # Reset questions
        self.num_questions.set(questions)

        # amount of questions structure
        question_amount = "{} Question/s Left...".format(questions)
        self.questions_total.config(text=question_amount)

        # question structure
        to_ask = "{} {} {} =".format(num, operation, random_number)
        self.show_questions.config(text=to_ask)

        if questions == -1:
            self.next_button.config(state=DISABLED)
            self.check_button.config(state=DISABLED)
            question_amount_finish = "No more Question/s Left..."
            self.questions_total.config(text=question_amount_finish)
            self.questions_total.config(fg="maroon")
            to_ask_nomore = "..."
            self.show_questions.config(text=to_ask_nomore)
            self.show_questions.config(fg="black")
            self.user_input.config(state=DISABLED)
            print("----------")
            print("No more questions...")

        else:
            self.next_button.config(state=DISABLED)

    def check_function(self):

        # **** variables included ****
        user_input = self.user_input.get()
        num = self.num_to_use.get()
        operation = self.num_operation.get()

        # retrieve random_number
        random_number = self.num_random.get()

        # correct answer structure
        to_answer = eval("{} {} {}".format(num, operation, random_number))
        self.user_input.config(text=to_answer)

        # Set error background colours (and assume that there are no
        # errors at the start...
        incorrect_back = "maroon"
        correct_back = "#008000"
        correct = "no"
        incorrect = "no"
        answer_feedback = ""
        stats_correct = 0
        stats_incorrect = 0

        try:
            user_input = int(user_input)

            if user_input == to_answer:
                correct = "yes"
                answer_feedback = "Correct!"
                print("----------")
                print("Correct!")
                self.check_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)
                stats_correct += 1

            elif user_input > to_answer or user_input < to_answer:
                incorrect = "yes"
                answer_feedback = "Incorrect, try again..."
                print("----------")
                print("Incorrect, try again...")
                self.check_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)
                stats_incorrect += 1

            else:
                self.check_button.config(state=NORMAL)



        except ValueError:
            correct = "yes"
            incorrect = "yes"
            answer_feedback = "Entry Error (blank / no decimals or text)"

        if incorrect == "yes":
            self.user_input.config(bg=incorrect_back)
            self.math_quiz_amount_error_label_1.config(fg=incorrect_back)
            self.math_quiz_amount_error_label_1.config(text=answer_feedback)

        elif correct == "yes":
            self.user_input.config(bg=correct_back)
            self.math_quiz_amount_error_label_1.config(fg=correct_back)
            self.math_quiz_amount_error_label_1.config(text=answer_feedback)

        incorrect_tostats = "Incorrect: {}".format(stats_incorrect)
        self.incorrect_list.append(incorrect_tostats)
        print(self.incorrect_list)

        correct_tostats = "Correct: {}".format(stats_correct)
        self.correct_list.append(correct_tostats)
        print(self.correct_list)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)

    def to_stats(self, question_stats, incorrect_tostats, correct_tostats):
        GameStats(self, question_stats, incorrect_tostats, correct_tostats)

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


class GameStats:
    def __init__(self, partner, question_stats, incorrect_tostats, correct_tostats):
        print("----------")
        print("===== Game Statistics =====")
        print("Questions: {}".format(question_stats))
        print("Correct: {}".format(correct_tostats))
        print("Incorrect: {}".format(incorrect_tostats))

        # **** initialise variables ****
        self.num_questions = IntVar()
        # amount of questions entered by user
        self.num_questions.set(question_stats)

        # GUI Setup
        self.stats_box = Toplevel()

        # If users press cross at top, game quits
        self.stats_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Heading Row
        self.heading_label = Label(self.stats_frame, text="Game Statistics",
                                   font="Arial 24 bold", padx=10,
                                   pady=10, width=20)
        self.heading_label.grid(row=0)

        self.instructions_label = Label(self.stats_frame, wrap=300, justify=LEFT,
                                        text="Here are your Game Statistics. Please use "
                                             "the Export button to access the results "
                                             "each question that have been answered. ",
                                        font="Arial 10", padx=10, pady=10, fg="green")
        self.instructions_label.grid(row=1, pady=20)

        self.questions_answered_frame = Frame(self.stats_box)
        self.questions_answered_frame.grid(row=2)

        self.questions_correct_frame = Frame(self.stats_box)
        self.questions_correct_frame.grid(row=3)

        self.questions_incorrect_frame = Frame(self.stats_box)
        self.questions_incorrect_frame.grid(row=4)

        self.export_dismiss_frame = Frame(self.stats_box)
        self.export_dismiss_frame.grid(row=5)

        self.questions_answered = Label(self.questions_answered_frame,
                                        text=question_stats[0],
                                        font="Arial 12 bold")
        self.questions_answered.grid(row=0, column=0)

        self.questions_correct = Label(self.questions_correct_frame,
                                       text="Questions Correct: {}".format(correct_tostats), font="Arial 12 bold")
        self.questions_correct.grid(row=0, column=0)

        self.questions_incorrect = Label(self.questions_incorrect_frame,
                                         text="Questions Incorrect: {}".format(incorrect_tostats), font="Arial 12 bold")
        self.questions_incorrect.grid(row=0, column=0)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_stats(self, partner):
        # put Help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz Game")
    something = Start(root)
    root.mainloop()
