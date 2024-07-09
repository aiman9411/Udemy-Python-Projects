from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    second = count % 60
    canvas.itemconfig(canvas_text, text= f"{min}:{second}")
    if count > 1:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 112, fill="white", font=(FONT_NAME, 35, "normal"))
canvas.grid(row=1, column=1)


# Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
timer_label.grid(row=0, column=1)

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

# Tick Label
tick_label = Label(text="✅", bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()