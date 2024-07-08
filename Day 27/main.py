from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=200)

# Define function
def calculate():
    km_distance = float(input.get()) * 1.6
    number_label.config(text = km_distance)

#Input
input = Entry(width = 5)
input.grid(column = 2, row = 2, padx = 10, pady = 10)

#Miles Label
miles_label = Label(text = "Miles", font = ("Arial", 15, "normal"))
miles_label.grid(column = 3, row = 2)

# Is Equal To Label
equal_label = Label(text = "Is Equal To", font = ("Arial", 15, "normal"))
equal_label.grid(column=0, row= 3, padx=10)

# Number Label
number_label = Label(text = "", font = ("Arial", 15, "normal"))
number_label.grid(column = 2, row = 3, pady = 10)

# KM Label
km_label = Label(text = "KM", font = ("Arial", 15, "normal"))
km_label.grid(column = 3, row = 3)

# Button
button = Button(text="Calculate", command= calculate)
button.grid(column = 2, row = 4)

window.mainloop()