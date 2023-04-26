from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH METHOD ------------------------------- #


def search():

    searched_website = website_entry.get()
    if len(searched_website) == 0:
        messagebox.showerror("ooops", "Please give me the website name u are looking for!")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror("ooops", "Can't find the file!")
        else:
            try:
                searched_email = data[searched_website]["email"]
                searched_password = data[searched_website]["password"]
            except KeyError:
                messagebox.showerror("ooops", "Can't find the website u are looking for!")
            else:
                messagebox.showinfo(searched_website, f"Email: {searched_email}\n Password: {searched_password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # Automatikusan vágólapra másolás
    pyperclip.copy(password)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    current_website = website_entry.get()
    current_email = email_entry.get()
    current_password = password_entry.get()
    new_data = {current_website:
        {
            "email": current_email,
            "password": current_password,
        }
    }

    if len(current_website) == 0 or len(current_password) == 0:
        messagebox.showerror("Error!", message="Website and/or Password cannot be empty!")

    else:
        try:
            with open("passwords.json", "r") as data_file:
                # JSON fáljba írás
                # json.dump(new_data, data_file, indent=4)

                # JSON-ból olvasás
                # data = json.load(data_file)
                # print(data)

                # JSON UPDATE/hozzáírás
                # Régi adat beolvasása
                data = json.load(data_file)
                # régi adat frissítése új adattal

        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                # új adat kimentése
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as data_file:
                # új adat kimentése
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, columnspan=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

e_mail_label = Label(text="Email/Username:")
e_mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus()  # egyből ide teszi le a kurzort

email_entry = Entry(width=60)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "davidholecska@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# Buttons
add_button = Button(text="Add", width=51, command=save)
add_button.grid(column=1, columnspan=2, row=4)

gen_pass_button = Button(text="Generate Password", width=21, command=generate_password)
gen_pass_button.grid(row=3, column=2)

search_button = Button(text="Search", width=21, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
