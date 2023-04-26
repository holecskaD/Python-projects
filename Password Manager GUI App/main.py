from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
add_button = Button(text="Add", width=51)
add_button.grid(column=1, columnspan=2, row=4)

gen_pass_button = Button(text="Generate Password", width=21)
gen_pass_button.grid(row=3, column=2)



window.mainloop()