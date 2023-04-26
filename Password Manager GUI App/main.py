from tkinter import *
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=200, pady=200)
canvas = Canvas(width=400, height=424, bg=YELLOW)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(200, 190, image=lock_img)
canvas.grid(column=1, row=0)











window.mainloop()