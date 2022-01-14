import csv
from tkinter import *
import pandas as pd
import random
from os import path

LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"

current_card = ()
known_words = []

# functions


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    fr, en = random.choice(fr_en_list)
    canvas.itemconfig(word, text=fr)
    current_card = (fr, en)
    flip_frnt()
    window.after(3000, func=flip_card)


def create_csv():
    with open("data/unknown_words.csv", "w") as f:
        csv_out = csv.writer(f)
        csv_out.writerow(["French", "English"])
        for row in fr_en_list:
            csv_out.writerow(row)

    with open("data/known_words.csv", "w") as f:
        csv_out = csv.writer(f)
        csv_out.writerow(["French", "English"])
        for row in known_words:
            csv_out.writerow(row)


def right_click():
    known_words.append(current_card)
    print(f"size before known word: {len(fr_en_list)}")
    fr_en_list.remove(current_card)
    next_card()
    create_csv()
    print("known words:", known_words)
    print(f"size after known word: {len(fr_en_list)}")


def flip_frnt():
    canvas.itemconfig(lang, text="FRENCH", fill="black")
    canvas.itemconfig(word, text=current_card[0], fill="black")
    canvas.itemconfig(card_background, image=card_image_frnt)


def flip_back():
    canvas.itemconfig(lang, text="ENGLISH", fill="white")
    canvas.itemconfig(word, text=current_card[1], fill="white")
    canvas.itemconfig(card_background, image=card_image_back)


def flip_card():
    # card_lang = canvas.itemcget(lang, "text")
    # if card_lang == "FRENCH":
    flip_back()
    # else:
    #     flip_frnt()


# get data from the unkown_words.csv if it exists else from default csv
if path.exists("data/unknown_words.csv"):
    data = pd.read_csv("data/unknown_words.csv")
else:
    data = pd.read_csv("data/french_words.csv")

fr_en_list = list(zip(data.French, data.English))

window = Tk()
window.title("Flashy French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_image_frnt = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_image_frnt)


lang = canvas.create_text(400, 150, text="FRENCH", font=LANG_FONT)
word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image_btn = PhotoImage(file="images/wrong.png")
wrng_btn = Button(image=wrong_image_btn, highlightthickness=0, command=next_card)
wrng_btn.grid(row=1, column=0)

right_image_btn = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image_btn, highlightthickness=0, command=right_click)
right_btn.grid(row=1, column=1)

# while True:
flip_timer = window.after(3000, func=flip_card)
next_card()

window.mainloop()
