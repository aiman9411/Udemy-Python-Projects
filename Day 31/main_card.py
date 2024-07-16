from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
DARKER_GREEN = '#3C8D6B'

# Create UI
window = Tk()
window.title("Language Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.geometry("800x600")

canvas = Canvas(window, width=700, height=400, bg=BACKGROUND_COLOR)
canvas.grid(column=1, row=1, padx=50, pady=50)
canvas.create_rectangle(0, 0, 700, 400, fill=DARKER_GREEN, outline="")

window.mainloop()