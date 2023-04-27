from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
actual_word_pair = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=actual_word_pair["English"], fill="white")


def new_word():
    global actual_word_pair
    global timer
    window.after_cancel(timer)
    actual_word_pair = random.choice(to_learn)
    actual_word_french = actual_word_pair["French"]
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=actual_word_french, fill="black")
    timer = window.after(3000, flip_card)


def known_word():
    to_learn.remove(actual_word_pair)
    new_csv_data = pandas.DataFrame(to_learn)
    new_csv_data.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    new_word()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 270, image=card_front_img)

canvas.grid(column=0, row=0, columnspan=2)

# Texts
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 253, text="Word", font=("Ariel", 60, "bold"), fill="black")

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
right_button = Button(image=right_image, highlightthickness=0, command=known_word)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)
new_word()


window.mainloop()
