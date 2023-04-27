import time
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"

#---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 270, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button = Button(image=right_image, highlightthickness=0)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()