
# if users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

# Quit Button (row 12)
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=12, column=1)


# button frame (row 8)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=8)

def to_quit(self):
    root.destroy()