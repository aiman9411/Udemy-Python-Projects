from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    return ''.join(password_list)
   
def display_password():
    password = gen_password()
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_website():
    website_input = website_entry.get()
    return website_input

def get_email():
    email_input = email_entry.get()
    return email_input

def get_password():
    password_input = password_entry.get()
    return password_input

def save_info():
    website = get_website()
    email = get_email()
    password = get_password()

    with open("data.txt", "a") as file:
        file.write(website + " | " + email + " | " + password + "\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def message_box():
    website = get_website()
    email = get_email()
    password = get_password()
    response = messagebox.askyesno(title="Password Confirmation", message=f"Website: {website} \nEmail: {email} \nPassword: {password} \nDo you want to proceed with the password?")
    if response:
        save_info()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label 
website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)

# Email Label 
email_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_label.grid(row=2, column=0)

# Password Label 
password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(row=3, column=0)

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"aimannazmi59@gmail.com")

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# Generate Password Button
generate_button = Button(text="Generate Password", command=display_password)
generate_button.grid(row=3, column=2)

# Add Password Button
add_button = Button(text="Add", width=36, command=message_box)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()