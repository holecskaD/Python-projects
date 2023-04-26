from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    #Automatikusan vágólapra másolás
    pyperclip.copy(password)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    current_website = website_entry.get()
    current_email = email_entry.get()
    current_password = password_entry.get()
    if len(current_website) == 0 or len(current_password) == 0:
        messagebox.showerror("Error!", message="Website and/or Password cannot be empty!")

    else:
        is_ok = messagebox.askokcancel(title=current_website,
                                       message=f"These are the details entered: \n {current_email} \n {current_password} "
                                               f"\n Is it OK to save? ")
        if is_ok:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{current_website} | {current_email} | {current_password}\n")
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

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

e_mail_label = Label(text="Email/Username:")
e_mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=60)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus() #egyből ide teszi le a kurzort

email_entry = Entry(width=60)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "davidholecska@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

#Buttons
add_button = Button(text="Add", width=51, command=save)
add_button.grid(column=1, columnspan=2, row=4)

gen_pass_button = Button(text="Generate Password", width=21, command=generate_password)
gen_pass_button.grid(row=3, column=2)




window.mainloop()