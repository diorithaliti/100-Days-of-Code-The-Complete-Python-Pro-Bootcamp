import csv
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_body, text= current_card["French"], fill="Black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_body, text= current_card["English"], fill="White")
    canvas.itemconfig(canavas_background, image=card_back_img)
    window.after(3000, func=next_card)
def delete_item():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv")
    next_card()


#UI


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=30, pady=30)

flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")
canavas_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_body = canvas.create_text(400, 264, text="", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0, )

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command = lambda:[next_card(), delete_item()])
right_button.grid(row=1, column=1)

next_card()




window.mainloop()

