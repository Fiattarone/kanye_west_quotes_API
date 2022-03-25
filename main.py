import requests
from tkinter import *


def get_quote():
    global kanye_quote
    response = requests.get(url="http://api.kanye.rest")
    response.raise_for_status()

    data = response.json()  # Parsed for JSON
    kanye_quote = data["quote"]
    print(len(kanye_quote))
    font_size = 20
    if len(kanye_quote) > 80:
        font_size = 15
    if len(kanye_quote) > 170:
        font_size = 12
    canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", font_size, "bold"))


window = Tk()
window.title("What's Kanye Saying?")
window.config(width=50, height=50)

kanye_quote = ""

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 287, image=background_image)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Arial",  20, "bold"), fill="white")
canvas.grid(row=0, column=0)

get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()

