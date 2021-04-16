import requests
from tkinter import *
from random import choice, randint
from PIL import ImageTk, Image

BACKGROUND = '#32527b'


def random_color():
    random_number = randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]

    return hex_number


def get_quotes():
    url = "https://www.quotepub.com/api/widget/?type=rand&limit=100"

    data = requests.get(url=url).json()

    quotes = [[quote['quote_body'], quote['quote_author']] for quote in data]

    random_quote = choice(quotes)
    canvas.itemconfig(quote_text, text="\n\n".join(random_quote))


# ____________________________________________UI_SETUP___________________________________#

window = Tk()
window.title(f'Message Says')
window.minsize(width=400, height=400)
window.config(padx=20, pady=20, bg=BACKGROUND)
canvas = Canvas(width=626, height=626, bg=BACKGROUND, highlightthickness=0)
photo_image = ImageTk.PhotoImage(Image.open('Quote.JPG'))
canvas.create_image(300, 260, image=photo_image)
quote_text = canvas.create_text(300, 207, text="", width=250, font=("Arial", 12, "bold"),
                                fill=random_color())
canvas.grid(row=0, column=0)

button_image = ImageTk.PhotoImage(Image.open('button.gif'))
quote_button = Button(image=button_image, highlightthickness=0, command=get_quotes)
quote_button.grid(row=1, column=0)

window.mainloop()
