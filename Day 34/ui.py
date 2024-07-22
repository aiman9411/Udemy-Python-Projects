from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(self.window, width=300, height=250)
        self.news = self.canvas.create_text(100, 100, text="Amazon", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column = 0, row= 1, columnspan=2)

        self.label = Label(text="Score: 0", font=("Arial", 15, "normal"),foreground="white")
        self.label.config(bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.right_image = PhotoImage(file="true.png")
        self.cross_button = Button(image=self.right_image, highlightthickness=0)
        self.cross_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()