from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Getting Hold of values Entered in Entry component using Get Method.
    website = website_entry.get()
    email_username = email_username_entry.get()
    passwords = password_entry.get()

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you have not left any field.")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: "
                                                                f"\nEmail: {email_username} "
                                                        f"\nPassword: {passwords} \nIs it okay to save.")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email_username}|{passwords }\n")
                # Deleting previous Entry and Making place for new Entry using Delete Method.
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
canva_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canva_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus() # Automatically points cursor into website Entry.

email_username_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "seif.shaikh2021@gmail.com") # Inserts a pre-defined text in email-Entry.

password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add",  width=36, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
