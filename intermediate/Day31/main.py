from tkinter import Tk, Canvas, PhotoImage, Button
from pandas import read_csv, DataFrame
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn ={}

# French Words
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# functions
def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    # choose new word
    curr_card = choice(to_learn)
    # canvas config
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card['French'], fill="black")
    # flip card only will run one time in the code but we needed everytime a new card creates
    # flip card
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card['English'], fill="white")

def is_known():
    to_learn.remove(curr_card)
    data_frame = DataFrame(to_learn)
    data_frame.to_csv("data/words_to_learn.csv", index=False)

    next_card()



# Window 
window = Tk()
window.title("Flashy French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flip card
flip_timer = window.after(3000, func=flip_card)

# Background image
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

# canvas config
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400,263, image=card_front_image)

# Canvas Text
card_title = canvas.create_text(400, 150, text="Title", font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=('Arial', 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
# end of Background image

# unkonwn button
unknown_btn_img = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=unknown_btn_img, command=next_card)
unknown_btn.grid(row=1, column=0)
# End of unkonwn button

# known button
known_btn_img = PhotoImage(file="images/right.png")
known_btn = Button(image=known_btn_img, command=is_known)
known_btn.grid(row=1, column=1)
# End of known button


next_card()
window.mainloop()